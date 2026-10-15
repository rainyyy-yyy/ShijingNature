# 《詩經・國風》：情景關係的數位人文考察

## 專案簡介
本專案為2026 DADH研討會論文所使用之程式，旨在針對《詩經・國風》中各個情感主題的自然意象進行詞頻分析，並在後續於 Excel 中進行調整後標準化殘差（Adjusted Standardized Residual）計算，用以進行後續論文之質性探討。

---

## 程式執行
1. 一次執行會跑完該資料夾下的所有資料夾內的文本，可透過修改程式第 15 行之資料夾決定要進行統計的情感主題分類
2. 輸出結果會在output資料夾中，名稱為輸入資料夾路徑的最後一層資料夾名稱，可通過修改程式第 17 行之資料夾決定輸出結果儲存位置
3. 程式使用 Python 程式語言撰寫，需先配置執行環境，並確定是否有 `pandas` 與 `matplotlib`，若無則須於終端機（Terminal）執行以下指令配置：
``` 
pip install pandas matplotlib
```
4. 配置環境後，於終端機執行以下指令切換到程式資料夾
```
cd ShijingNature/
```
5. 切換至程式所在資料夾後，在終端機執行以下指令即可針對該情感主題進行自然意象詞彙之詞頻統計
```
python run.py
```

---

## 論文摘要
&emsp;&emsp;《詩經‧國風》大量運用自然物色，然而既有研究多從個別篇章說明物與情相應，缺少對全體文本的檢驗。本研究以〈國風〉一百六十篇為對象，建構七大物色類別與六大情感主題分類，運用詞頻分析、交叉分析、卡方檢定及調整後標準化殘差，檢視物色選擇與情感主題的對應規律。研究共標註 1,267 詞次物色意象，卡方檢定（χ²= 227.584，df = 30，p < 0.001）顯示物色分布與情感主題顯著相關。殘差分析進一步呈現由大類至子類別的雙層「功能鎖定」傾向（即顯著的偏好或規避關係）：宏觀上，植物意象僅少數格達顯著，動物意象則呈兩極分化；細分子類別後，穀物與獸類偏向勞作、征役等寫實主題，花卉、鳥禽與魚類在愛情與婚姻中多呈正殘差。微觀上，部分關聯高度集中，如時序季節之於勞作生活，惟此類極端關聯依賴〈豳風‧七月〉等少數篇章，仍待敏感度分析檢驗。此外，水域意象僅占全部詞次的 9.31%，其文學重要性可能來自愛情篇章中的集中使用，而非總量。本研究結果與傳統詩學劉勰「物色相召」的方向並不衝突，但本研究所測為物色類別與主題的統計關聯，與心物感應的詮釋層次不同，仍須由文本詮釋接榫。研究並提供可重複運用的量化分析框架，展現數位人文方法於古典詩學研究之潛力。 
**關鍵字：**《詩經‧國風》、物色、情感主題、詞頻分析、調整後標準化殘差

&emsp;&emsp;*Nature imagery is widely used in the Guofeng of the Shijing (Book of Songs), yet previous studies have mostly examined imagery–emotion correspondence through individual poems, with limited analysis of the whole corpus. This study analyzes all 160 Guofeng poems using seven imagery categories and six emotional themes. Wordfrequency analysis, cross-tabulation, chi-square tests, and adjusted standardized residuals were applied to 1,267 annotated instances. Imagery distribution was significantly associated with emotional themes (χ² = 227.584, df = 30, p < 0.001), revealing a two-level pattern of “functional locking,” or significant preference and avoidance, from major categories to subcategories. Plant imagery showed significance in only a few cells, while animal imagery was polarized; at the subcategory level, grains and beasts were associated with realistic themes, whereas flowers, birds, and fish showed positive residuals in love and marriage poems. Seasonal imagery was strongly associated with labor and everyday life, although such associations depended on a small number of poems. Water imagery accounted for only 9.31% of instances, suggesting that its literary significance may derive from concentrated use in love poems rather than overall frequency. The findings are consistent with the direction of Liu Xie’s concept of “wuse xiangzhao” (objects and appearances mutually evoke one another), while statistical associations still require textual interpretation. This study provides a reproducible quantitative framework and demonstrates the potential of digital humanities methods for classical Chinese poetics.
**Keywords:** Guofeng of the Shijing; natural imagery; emotional themes; word-frequency analysis; adjusted standardized residuals*
