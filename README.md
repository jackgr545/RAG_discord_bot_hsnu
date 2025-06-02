# 師大附中校園導覽機器人

這是一個專為 **師大附中** 設計的校園導覽 Discord 機器人，使用 Python 開發，整合多種 API 並搭配 Gemini 語言模型，提供互動式語言生成與即時導航功能。

---

## 功能簡介

- 使用 [Gemini API](https://aistudio.google.com/apikey) 進行自然語言生成，根據使用者輸入提供智能回應。
- 整合 [SerpAPI](https://serpapi.com/)，可在 Discord 中直接搜尋 Google 網頁內容。
- 利用 [Google Maps API](https://developers.google.com/maps) 提供即時的路線規劃與導航服務。
- 額外支援 [NASA API](https://api.nasa.gov/)，每日推送美麗的星空照片，讓校園導覽增添一點浪漫氛圍。  
  > （雖然跟校園導覽無關，但增添趣味與氣氛！）

---

## 安裝方式

### 方式一：使用 Git 克隆專案

1. 在任意位置建立一個新資料夾，並用 VSCode 開啟終端機 (Terminal)。
2. 輸入以下指令下載專案：

    ```bash
    git clone https://github.com/jackgr545/RAG_discord_bot_hsnu.git
    cd RAG_discord_bot_hsnu
    ```

3. 確認你的 Python 版本為 3.10（建議使用虛擬環境，避免版本衝突）。
4. 安裝專案所需套件：

    ```bash
    pip install -r requirements.txt
    ```

5. 將 `example.env` 複製並重新命名為 `.env`，並依說明設定你的 API 金鑰與環境變數。

---

### 方式二：手動下載 ZIP 檔

1. 在 GitHub 專案頁面點選「Code」按鈕，選擇「Download ZIP」下載專案壓縮檔。![螢幕擷取畫面 2025-06-02 172622](https://github.com/user-attachments/assets/50767b45-94d0-407f-ae28-b5d03bc4950c)

2. 將 ZIP 檔解壓縮後，將裡面所有檔案拖曳到你新建立的資料夾中。

3. 進入資料夾，確認 Python 版本為 3.10，並安裝需求套件：

    ```bash
    pip install -r requirements.txt
    ```

4. 將 `example.env` 複製並重新命名為 `.env`，依指示填寫環境變數。

---
