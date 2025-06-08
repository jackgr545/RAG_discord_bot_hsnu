# 師大附中校園導覽機器人

這是一個專為 **師大附中** 設計的校園導覽 Discord 機器人，使用 Python 開發，整合多種 API 並搭配 Gemini 語言模型，提供互動式語言生成與即時導航功能。


[架構簡圖](https://github.com/user-attachments/assets/f4de69d1-de4d-4dfe-9940-0591b335b9d6)
[google_map功能簡圖](https://github.com/user-attachments/assets/ee66c567-ddf9-4147-bdb3-69b0473f0974)



## 功能簡介

- 使用 [Gemini API](https://aistudio.google.com/apikey) 進行自然語言生成，根據使用者輸入提供智能回應。
- 整合 [SerpAPI](https://serpapi.com/)，可在 Discord 中直接搜尋 Google 網頁內容。
- 利用 [Google Maps Direction_API](https://developers.google.com/maps/documentation/directions/?hl=zh_TW) 提供即時的路線規劃與導航服務。
- 額外支援 [NASA API](https://api.nasa.gov/)，每日推送美麗的星空照片，讓校園導覽增添一點浪漫氛圍。  
  > （雖然跟校園導覽無關，但增添趣味與氣氛！）

## 針對新手的詳細指引
如果您是新手，請參考`detailed_guides.md`。
[詳細的安裝步驟與API設定](detailed_guides.md)
## 安裝步驟

**注意：** 需要 Python 3.10 版本

### 方法1：Git 下載
```bash
git clone https://github.com/jackgr545/RAG_discord_bot_hsnu.git
cd RAG_discord_bot_hsnu
pip install -r requirements.txt
```

### 方法2：ZIP 下載
1. 到 GitHub 下載 ZIP 檔案並解壓縮
2. 安裝依賴：`pip install -r requirements.txt`



## API 設定

將 `example.env` 複製為 `.env`，並填入以下 API 金鑰：

### 1. Discord Bot Token
- 到 [Discord Developer Portal](https://discord.com/developers/applications)
- 建立新應用程式 → Bot → 重設 Token
- 開啟所有 Bot 權限
- 複製 Token 到 `.env` 的 `DISCORD_TOKEN`

### 2. Discord 伺服器 ID
- Discord 設定開啟「開發者模式」
- 右鍵點擊伺服器名稱 → 複製伺服器 ID
- 填入 `.env` 的 `DISCORD_SERVER_ID`

### 3. Gemini API
- 到 [Google AI Studio](https://aistudio.google.com/apikey)
- 建立 API 金鑰
- 填入 `.env` 的 `GEMINI_API`

### 4. SerpAPI (搜尋功能)
- 到 [SerpAPI](https://serpapi.com/) 註冊帳號
- 複製 API 金鑰
- 填入 `.env` 的 `SERPAPI_API_KEY`

### 5. Google Maps API (需信用卡)
- 到 [Google Cloud Console](https://console.cloud.google.com)
- 啟用 Directions API
- 建立 API 金鑰並限制只能使用 Directions API
- 填入 `.env` 的 `GOOGLE_MAPS_API`

### 6. NASA API
- 到 [NASA API](https://api.nasa.gov/) 申請
- 填寫 Email 即可獲得 API 金鑰
- 填入 `.env` 的 `NASA_API`

## 重要提醒

- **絕對不要分享你的 API 金鑰**
- Google Maps API 需要信用卡驗證（有90天免費額度）
- 建議使用 Python 虛擬環境避免版本衝突


## 執行

1. 在TERMINAL中輸入以下指令
   
    ```bash
    python main.py
    ```
    
2. 如果成功執行terminal 上會有如下輸出

  ![螢幕擷取畫面 2025-06-02 212454](https://github.com/user-attachments/assets/9bdd9672-bf0f-4764-b8af-54bdd303a260)

3. 可以去discord 中測試機器人了喔!!

