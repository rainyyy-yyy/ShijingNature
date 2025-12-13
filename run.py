import os
import re
import csv
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
from matplotlib import rcParams

# ===== 設定中文字型 =====
rcParams['font.sans-serif'] = ['Microsoft JhengHei']  # Windows 中文字型
rcParams['axes.unicode_minus'] = False

# ===== 使用前設定 =====
text_folder = "D:/Users/peggy/Github/ShijingNature/shijing"  # txt 檔資料夾
word_csv = "D:/Users/peggy/Github/ShijingNature/shijing/test.csv"  # 詞彙對照表 (三欄：詞, 大類, 子類)
exclude_csv = "D:/Users/peggy/Github/ShijingNature/shijing/exclude.csv"  # 要排除統計的詞彙表 (一欄：詞)
output_folder = "output/shijing"  # 輸出結果資料夾
os.makedirs(output_folder, exist_ok=True)

# ===== 清理文字：只保留中文字 =====
def clean_text(text):
    return re.sub(r"[^\u4e00-\u9fa5]", "", text)


# ===== 載入排除詞彙 =====
def load_excluded_words(csv_path):
    excluded = set()
    if os.path.exists(csv_path):
        with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.reader(f)
            next(reader, None)  # 若有標題列可保留
            for row in reader:
                if len(row) > 0:
                    excluded.add(row[0].strip().replace("\ufeff", ""))
    return excluded


# ===== 長詞優先、不重疊統計 =====
def find_nonoverlapping_counts(text, words):
    # 按詞長排序：長詞先掃
    sorted_words = sorted(words, key=len, reverse=True)
    used = [False] * len(text)  # 標記哪些字已被覆蓋
    word_counts = Counter()

    # 標記排除詞彙，但不列入統計
    for ex_word in sorted(excluded_words, key=len, reverse=True):
        for match in re.finditer(re.escape(ex_word), text):
            start, end = match.span()
            for i in range(start, end):
                used[i] = True  # 標記但不計數

    # 長詞優先：先統計長詞並標記
    for word in sorted_words:
        for match in re.finditer(re.escape(word), text):
            start, end = match.span()
            # 若該範圍都沒被佔用才統計
            if not any(used[start:end]):
                word_counts[word] += 1
                for i in range(start, end):
                    used[i] = True  # 標記已佔用
    return word_counts


# ===== 讀取詞彙分類表 =====
word_map = {}
with open(word_csv, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.reader(f)
    header = next(reader, None)
    for row in reader:
        if len(row) < 3:
            continue
        word = row[0].strip().replace("\ufeff", "")
        if not word:
            continue
        main_cat = row[1].strip()
        sub_cat = row[2].strip()
        word_map[word] = (main_cat, sub_cat)

# ===== 載入排除詞 =====
excluded_words = load_excluded_words(exclude_csv)

# ===== 合併所有 txt 檔 =====
all_text = ""
for filename in os.listdir(text_folder):
    if filename.endswith(".txt"):
        with open(os.path.join(text_folder, filename), "r", encoding="utf-8") as f:
            all_text += clean_text(f.read())

# ===== 詞頻統計（避免重疊） =====
word_counts = find_nonoverlapping_counts(all_text, list(word_map.keys()))
main_counter = Counter()
sub_counter = defaultdict(Counter)

for word, count in word_counts.items():
    main_cat, sub_cat = word_map[word]
    main_counter[main_cat] += count
    sub_counter[main_cat][sub_cat] += count

# ===== 建立輸出資料結構 =====
data_rows = []
for main_cat, total in main_counter.most_common():
    data_rows.append([main_cat, total, "", ""])
    for sub_cat, sub_total in sub_counter[main_cat].most_common():
        # 這裡 sub_cat 本身就是詞或子類
        data_rows.append(["", "", sub_cat, sub_total])


# ===== 儲存為 CSV 檔 =====
output_file = os.path.join(output_folder, "category_stats.csv")
df = pd.DataFrame(data_rows, columns=["大類", "總數", "子類", "子類數"])
df.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"統計完成！已輸出到 CSV：{output_file}")

# ===== 全體大類長條圖 =====
plt.figure(figsize=(10,6))
cats, counts = zip(*main_counter.most_common())
plt.bar(cats, counts, color="#78C8EB")
plt.title("Word Frequency by Main Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=30, ha='right')

# ===== 顯示數值標籤 =====
for i, v in enumerate(counts):
    plt.text(i, v - 0.5, str(v), ha='center', va='top', color='black', fontsize=10)

plt.tight_layout()

# ===== 儲存全體圖 =====
overall_chart = os.path.join(output_folder, "category_stats.png")
plt.savefig(overall_chart, dpi=300, bbox_inches='tight')
print(f"已輸出總覽圖：{overall_chart}")
plt.close()

# ===== 為每個大類輸出子類長條圖 =====
for main_cat, sub_dict in sub_counter.items():
    sub_cats, sub_counts = zip(*sub_dict.most_common())
    plt.figure(figsize=(8,5))
    plt.bar(sub_cats, sub_counts, color="#F6EF95")
    plt.title(f"Subcategory Frequency in {main_cat}")
    plt.xlabel("Subcategory")
    plt.ylabel("Count")
    plt.xticks(rotation=30, ha='right')

    # 在長條上方標註數值
    for i, v in enumerate(sub_counts):
        plt.text(i, v - 0.5, str(v), ha='center', va='top', color='black', fontsize=10)

    plt.tight_layout()
    sub_chart = os.path.join(output_folder, f"{main_cat}_subcategories.png")
    plt.savefig(sub_chart, dpi=300, bbox_inches='tight')
    print(f"已輸出 {main_cat} 類圖：{sub_chart}")
    plt.close()