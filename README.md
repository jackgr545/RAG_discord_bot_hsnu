#  師大附中校園導覽機器人

這是一個專為師大附中設計的校園導覽 Discord 機器人，使用 Python 開發，整合多種 API 並搭配 Gemini 語言模型，提供互動式的語言生成與導航體驗。



## 功能簡介

-  使用 [Gemini API](https://aistudio.google.com/apikey) 根據輸入資料進行自然語言生成。
-  整合 [SerpAPI](https://serpapi.com/) 搜尋 Google 網頁內容。
-  利用 [Google Maps API](https://developers.google.com/maps) 提供即時導航功能。
-  額外支援 [NASA API](https://api.nasa.gov/) 顯示每日星空美照  
  > ~~雖然和校園導覽無關，但很浪漫就對了~~ 



###安裝方式
1.使用指令安裝(如果你有git)

隨意創建一個新的資料夾，並用vscode開啟，接著在terminal輸入以下指令:

```bash
git clone https://github.com/jackgr545/RAG_discord_bot_hsnu.git
cd RAG_discord_bot_hsnu
```

確保您的 python 版本在3.10，如有必要請安裝於虛擬環境中

```bash
pip install -r requirements.txt
```
將 example.env 更名為 .env

2.手動安裝

隨意創建一個新的資料夾，並用vscode開啟

接著下載zip檔
![下載zip檔](https://github.com/user-attachments/assets/04b7eae0-4f72-41a9-a958-32875a100a25)

解壓縮後拖入您剛剛創建的新資料夾，並將檔案從解壓縮後的資料夾中拖出

```bash
pip install -r requirements.txt
```

將 example.env 更名為 .env

