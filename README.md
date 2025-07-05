# 遙測與機器學習範例程式碼 (Remote Sensing & Machine Learning Examples)

本專案包含一系列的 Python 範例程式碼，旨在展示如何應用於遙測 (Remote Sensing) 影像分析與農業資料科學。內容涵蓋了從基礎的資料讀取、影像處理，到進階的機器學習模型訓練與應用。

## 環境建置 (Installation)

建議使用 Python 3.9 環境，並請透過 pip 安裝所需的套件：

```bash
pip install -r requirements.txt
```

**注意:** `GDAL` 的安裝可能較為複雜，請使用 GDAL-3.3.0-cp39-cp39-win_amd64.whl 安裝。
```bash
pip install GDAL-3.3.0-cp39-cp39-win_amd64.whl
```

## 遙測影像分析範例程式碼
[範例檔案下載連結](https://reurl.cc/r9rrQN)

## 目錄結構 (Directory Structure)

```
.
├── 01_Image/         # 存放範例影像，包含一般影像與無人機空拍圖 (UAV)
├── 02_Data/          # 存放表格式資料，如 Excel (.xlsx) 與 CSV (.csv) 檔案
├── 03_Result/        # 存放程式執行後產生的結果
├── 04_Model_saved/   # 存放訓練完成後儲存的機器學習模型
├── A01_...py         # 各項功能的主要範例腳本
├── ...
├── C01_設定檔.py      # 共用的設定檔模組
└── C02_模型儲存.py    # 共用的模型儲存模組
```

## 腳本說明 (Scripts Overview)

每個 `A` 系列的腳本都是一個獨立的功能展示，而 `C` 系列的腳本則是共用的輔助模組。

### 第一部分：基礎資料處理 (A01 ~ A07)
- `A01_Pandas讀取資料.py`: 使用 Pandas 讀取 Excel 檔案。
- `A02_OpenCV讀取圖片.py`: 使用 OpenCV 讀取並顯示一般影像。
- `A03_GDAL讀取圖片.py`: 使用 GDAL 讀取 TIF 地理空間影像，並獲取其空間資訊。
- `A04_OGR讀取shapefile.py`: 使用 OGR 讀取 Shapefile 向量資料。
- `A05_Glob路徑讀取.py`: 使用 Glob 批次讀取符合特定規則的檔案路徑。
- `A06_Path路徑解析.py`: 使用 Pathlib 解析檔案路徑，取得資料夾、檔名、副檔名。
- `A07_字串解析.py`: 透過字串處理，從檔名中提取特定資訊（如日期）。

### 第二部分：影像處理與分析 (A08 ~ A17)
- `A08_影像分層.py`: 將彩色影像分離為 B, G, R 單一圖層。
- `A09_灰階與二值化處理.py`: 影像灰階化與手動設定閾值的二值化處理。
- `A10_Otsu二值化.py`: 使用 Otsu's 方法自動找尋最佳閾值進行影像二值化。
- `A11_色彩空間轉換與影像遮罩.py`: 將影像轉換至 HSV 色彩空間，並依據顏色範圍建立遮罩。
- `A12_Numpy計算矩陣平均值.py`: 使用 Numpy 計算影像特定區域的像素平均值。
- `A13_用GDAL與OGR切割空拍影像.py`: 根據 Shapefile 的範圍切割 TIF 影像。
- `A14_空拍圖ROI影像分析.py`: 對切割後的 ROI 影像進行植生指標計算與分析。
- `A15_計算並記錄植生指標平均.py`: 批次計算多個植生指標，並將結果儲存至 CSV 檔案。
- `A16_繪製數值可視化圖表.py`: 使用 Matplotlib 繪製數據的 XY 散佈圖。
- `A17_繪製植生指標計算圖.py`: 將計算出的植生指標結果視覺化並存成新的 TIF 檔案。

### 第三部分：機器學習 (A18 ~ A28)
- `A18_資料集分割.py`: 使用 Scikit-learn 將資料集分割為訓練集與測試集。
- `A19_機器學習模型訓練.py`: 訓練多種迴歸模型 (隨機森林、類神經網路、SVR、線性迴歸)，並進行評估與儲存。
- `A20_機器學習模型讀取.py`: 載入已儲存的模型進行預測。
- `A21_交叉驗證.py`: 執行 K-fold 交叉驗證來評估模型穩定性。
- `A22_t-SNE特徵分布圖_範例.py`: t-SNE 降維視覺化範例 (使用鳶尾花資料集)。
- `A23_PCA主成分分析_範例.py`: PCA 降維視覺化範例 (使用鳶尾花資料集)。
- `A24_Kmeans分群模型_範例.py`: K-means 分群範例 (使用鳶尾花資料集)。
- `A25_t-SNE特徵分布實際應用.py`: 將 t-SNE 應用於專案資料，視覺化特徵分布。
- `A26_K-means分群實際應用.py`: 將 K-means 應用於專案資料，進行非監督式分群。
- `A27_基於特徵領域適應模型訓練.py`: 使用 DANN 模型進行特徵層級的領域適應 (Domain Adaptation) 訓練。
- `A28_基於實例領域適應模型訓練.py`: 使用 IWC 模型進行實例層級的領域適應訓練。

### 輔助模組 (C01 ~ C02)
- `C01_設定檔.py`: 集中管理資料讀取、特徵與標籤欄位名稱等設定。
- `C02_模型儲存.py`: 提供一個統一的函數來儲存不同類型的機器學習模型。

## 如何執行 (How to Run)

每個 `A*.py` 檔案都是一個獨立的範例，可以直接執行以觀察結果。

```bash
python A01_Pandas讀取資料.py
python A02_OpenCV讀取圖片.py
# ...以此類推
```

部分腳本依賴於前面腳本的產出，建議可以依序研究。
`C*.py` 檔案為被其他腳本引用的模組，不需單獨執行。

<br><br>
====================================<br>
如果喜歡這個教學內容<br>
歡迎訂閱Youtube頻道<br>
[Maso的萬事屋](https://www.youtube.com/playlist?list=PLG4d6NSc7_l5-GjYiCdYa7H5Wsz0oQA7U)<br>
或加LINE私下交流 LINE ID: mastermaso<br>
![LOGO](https://yt3.ggpht.com/ytc/AKedOLR7I7tw_IxwJRgso1sT4paNu2s6_4hMw2goyDdrYQ=s88-c-k-c0x00ffffff-no-rj)<br>


====================================<br>