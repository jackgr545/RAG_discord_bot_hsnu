# 師大附中校園導覽機器人

這是一個專為 **師大附中** 設計的校園導覽 Discord 機器人，使用 Python 開發，整合多種 API 並搭配 Gemini 語言模型，提供互動式語言生成與即時導航功能。


[架構簡圖](https://github.com/user-attachments/assets/4e1b49c5-88ac-4b4d-82c4-966004ba0b3e](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=drawio_xml_flowchart.txt&dark=auto#R%3Cmxfile%3E%3Cdiagram%20name%3D%22Python%20Functions%20Flowchart%22%20id%3D%22flowchart%22%3E1Zxbc9o4GIZ%2FjWd2bzo%2BHy5tbAhNk6YhbZLeMC4WwbuAGWNy6K9fnQzYUhNtApKZyUxlYTsvjz99J6vRrN7ieVCmq9lFkYG5ZurZs2bFmmkalunCf9DMC5nxXItMPJR5Rk%2FaTYzy34BO6nR2k2dg3TixKop5la%2Bak5NiuQSTqjGXlmXx1DxtWsybv3WVPgBmYjRJ5%2BzsbZ5VMzLrm95u%2FgzkD7P6NxtuQD5ZpPXJ9JusZ2lWPO1NWYlm9cqiqMho8dwDcwSv5kKu6%2F%2Fh062wEiwrkQtCcsFjOt%2FQ76Ylnhb6mh9piaNFPc3vo0EAf%2FAAzsMx0V691EDgTSF7eBA9zfIKjFbpBH3yBB8%2FnJtVizk8MuBwms%2FnvWJelPg6CxhTZ4ouY3XTr%2FIIygo8703R7zEAxQJU5Qs8hX5quZQpNSqbHj7tnpBRY5%2FtPZ36spQaxcP2zjtucEDR8TFGHIw%2BphdgaI4WOghsYGqRjmZCU%2FMtdE6YaH6oJS6iGvnwHp%2FA8pHhWxabZQYyCvENxkdgaciE2ePAhAx9LYgxOo8ap9%2FTAuhI9DhfT4oyg6MILpuuoZNqhzGD7ldRfSo3SzjJWcbQ7MKAzgQBWvaJrUUh%2BukaRksmxoRjgRBMrEV9vIptjAo6SR0tbbLS4eLdrXQXGafv4asiLbRZnLNi8Wuz%2Ft8Oc2oBZ%2BocCLHdcpg8xC4HsX8AxH0WsdlP1%2F9iQ30bn2Rr9JukHJ9DSj%2BSMQ54pB6K4mEOxmuQlpNZN5ltc5zXoB1rBZ9xzWtVZN1kZak0sOErBraAX%2FbwxNpObTrJMvMwJB2VVveZEzdgZDVQfEDBoa%2BFESpfwBKUaQX%2B%2BltDlZAFyxorWsAqCV7zz2Zdja%2FDgXKTbFmkK9Mizz%2FOseUgO%2BYLuTSPZZVfxGhi74iOPZTpbIu%2FHVl6Msy50YeJFniX4SjE6Y%2BFfYOLPgsC5bTb3lSq7V5waPuoaAktTAhy01ESGcGxhQfwI5yBw6w7dOsBxgmzzI%2FilOhqpRr1FYu5r6NSBibnkY1jFqwTY5yoe8jAUc0IU%2FdQ8%2B0B9g3wnIt0tUacI2jYxl7jI0CGTIpMUm2eyiPwZD6CS%2BYR1A6Z40ZYyodlCgsj%2FUC%2BWm8y9XWJTL9%2BPPIt03U6Jqlux%2Fww1zqP5Ye%2FcUhCjxqi1hvyw31aqENjDI29cKdjjAy6DtTrbcMMTEHDPES9fi1mmOvNYpGW%2Be9t5sVJKBRbZavrYeiuxPU9EsP4a5PPs%2FGqLBarqoMI25Yol%2BENhyFOlALSY9c13yWZqYMq1TCgmSlKUT3coSODAM90L3tt996lwv3OwCULeUwKqg4aY3s9GzJx%2FeCu52aVRNNNZGAwQ8XrPNJpPgpzokCv64Je51iaMlnecljSZvsALPJljoH52Pj2yZ0aVEsm1DsGaglvkYNHMK6K1fjfDi5oJrpIXdH3f7bCEfxOYDkBN2W6XE%2BLcgHKuoAnVaaJw%2Fg2ufRR7IGTnQMqdVn%2FZID2w%2BFohPMeHaU%2BCQ7EpEZsLebOkZO6dkPe7gxILUKODa1bE%2BUuiFoPvYpEZhrh95AwFfIwR9rwOMeFToIc4y4Vwp38yO0eY1sm44i3dcPBaPC2DNz%2FQf149AqkT3t3IX5LTtZ3kHSPoCOTYI%2B3XwMHYd%2Bmi9z3G1YaYdM9JaBSW5txzF%2F2jSKRZkSmHl4NaYAKsAdF%2B2T0PTeBF7t%2F2C4y8KcO8I%2FEWmoPM%2BFt9Wi72HDI4UnsOHS3u48OyHc6nfrgWLbsS23TGwxfOMyztALjSQG55Us4XGuoXx%2Fg1Y9L8jCmO%2BdO9FWIXMYmw3gyT8t8%2BjLOwLpChPNiSRjTTDbEPiPqozhHcJNXUNBFR%2FhJRNGH%2FbBE3IFU3BaDe5ovs33W43kxwQON7J3YNpuhUUcJTdTCZJuf7aE%2FWZM3dKkPwWYewgOoxhBOBTS617EZLxvv%2FEjYPBm0hlS0Dgcted00hua9KdP5GG%2FAZx0Km4SgMi7BLsZFPYaTIW5KJe5ykhA2g96jCQ9hcci2unbVnYOceuCdDnFLJvEBZ1Mlp7IWIX7UNPCIvG2p2zE5%2BzERwgjt1SBGG239RUwLwcjAUTBGDTbixiOylwY6F9zkQFsS1e%2FdZMhKTf6GnN2bqKDeJtAJ3qJuo74Q6o6TAWbtk3555zbDukYLqCdz7z%2FIHgDnv1HRqXWxKSeUC%2B3OVWkJUw8yRb8%2Buser37QEc5gfPoLGvT%2Bq2hRSHbGqeypVW0Kqe6zqWKVqW0h1zKpOVKp2hFQnrOq%2BStXue1UPVKr23qv6TKVq%2F72qhypVB0Kq%2B6zqzypV12HuDdkDVva5Utli0fGMlf1FqWyx8DhkZV8olS0WHy9Y2VdKZYsFyM%2Bs7EulssUi5HnXZIuFyC%2Bs7K9KZYvFyK9doy0WJC9Z2d%2BUyhaLkt9Y2dcqZZtiUZIje6RUtliU5Mi%2BUSpbLEpes7K%2FK5UtFiW%2Fs7J%2FKJUtFiV%2FsLJvlcoWi5IjVvadUtliUfKOlX2vVLZYlLxnZf9UKlssSv5kZdfb3hTpFguTIa%2F7p7T9Z4kFyltWd%2B%2FgDUB8aViW6cveCasiX1brvTtfoQlt2%2Fc1mJ1AtELeQSC33CHZahOnJBaXI16bVG2fVCwy33T28dpMW%2F8Yj1ewnczrJ8dKH69gRzlmhSdKe8qWWDJwxequ94Yp0i2WDdQiG8JNpcLF8oFaZEO4pVS4WEZQi2wIt5UKF0sJapEN4Y5K4bZYSlCLbAh3lQoXi9K1yMZLH6VvfWyxKJ3w3vsoffFjiwXOAedthGLhYoHzjPM%2BYnjwl1bvSoxcr5UYBUdIjGzOH219zqs7ONQ%2FoT9QgI7u0REdx8%2F7By%2F0QIh1V7l6VoPrmxfY%2BivPgb3aNVu%2FzmhtRyGM6GWv6HAMvo7tjYgRMzd62zTg4e5vC5PTd3%2Bh2Ur%2BAw%3D%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E))
[google_map功能簡圖](https://github.com/user-attachments/assets/1f167dbb-507b-4fbb-a665-f251d29f6e1c)


## 功能簡介

- 使用 [Gemini API](https://aistudio.google.com/apikey) 進行自然語言生成，根據使用者輸入提供智能回應。
- 整合 [SerpAPI](https://serpapi.com/)，可在 Discord 中直接搜尋 Google 網頁內容。
- 利用 [Google Maps Direction_API](https://developers.google.com/maps/documentation/directions/?hl=zh_TW) 提供即時的路線規劃與導航服務。
- 額外支援 [NASA API](https://api.nasa.gov/)，每日推送美麗的星空照片，讓校園導覽增添一點浪漫氛圍。  
  > （雖然跟校園導覽無關，但增添趣味與氣氛！）



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

5. 將 `example.env` 複製並重新命名為 `.env`，並依說明設定你的 API 金鑰。



### 方式二：手動下載 ZIP 檔

1. 在 GitHub 專案頁面點選「Code」按鈕，選擇「Download ZIP」下載專案壓縮檔。![螢幕擷取畫面 2025-06-02 172622](https://github.com/user-attachments/assets/50767b45-94d0-407f-ae28-b5d03bc4950c)

2. 將 ZIP 檔解壓縮後，將裡面所有檔案拖曳到你新建立的資料夾中。

3. 進入資料夾，確認 Python 版本為 3.10（建議使用虛擬環境，避免版本衝突），並安裝需求套件：

    ```bash
    pip install -r requirements.txt
    ```

4. 將 `example.env` 複製並重新命名為 `.env`，並依說明設定你的 API 金鑰。



## API 金鑰與環境變數設定

### DISCORD_TOKEN
1. 前往[DISCORD.DEV](https://discord.com/developers/applications)，點選右上角的New Application
   
   ![螢幕擷取畫面 2025-06-02 175737](https://github.com/user-attachments/assets/7d9db1a4-a064-4433-b796-e44fd0a703ea)
   
2. 幫機器人命名，並確保OAuth2 URL Generator下的bot跟bot permittion administrator有被勾選
   
  ![螢幕擷取畫面 2025-06-02 193631](https://github.com/user-attachments/assets/0f090ffc-fc99-4a9f-8ae7-469dad2a4e2f)
  
  ![螢幕擷取畫面 2025-06-02 193753](https://github.com/user-attachments/assets/09c7114d-7a80-49ec-bdf2-579f9b5c641b)
3. 複製Generated URL，貼到google的網址欄，即可邀請bot加入你的伺服器
   
  ![螢幕擷取畫面 2025-06-02 200857](https://github.com/user-attachments/assets/1ce2a407-1dba-45ff-ad77-d68e99dabe54)
  
4. 切到bot類別下，把你能打開的選項都打開
   
  ![螢幕擷取畫面 2025-06-02 201831](https://github.com/user-attachments/assets/706b6541-08df-4f6e-a957-fce7ab65adbb)

5. 按下Reset Token按鈕，並複製TOKEN，貼到`.env`中的DISCORD_TOKEN="**在這裡貼上您的token**"
   
  ![螢幕擷取畫面 2025-06-02 202038](https://github.com/user-attachments/assets/3dc2b358-e7fa-4551-bb76-0a4f1cffe564)
  
  請不要分享您的TOKEN給別人



### DISCORD_SERVER_ID

1. 確保你的discord有開啟開發者模式(設定>進階>開發者模式)

![螢幕擷取畫面 2025-06-02 202732](https://github.com/user-attachments/assets/554650d0-40d8-4e34-8fed-215903e0714c)

2. 到剛剛加入機器人的伺服器中取得(對著籃框區域按下右鍵)

![螢幕擷取畫面 2025-06-02 203142](https://github.com/user-attachments/assets/889df7b7-112b-4f21-884b-552b034b1fff)

3. 複製伺服器ID，貼到`.env`中的DISCORD_SERVER_ID =**在這裡貼上您的伺服器ID**



### GEMINI_API
1. 前往[Gemini API](https://aistudio.google.com/apikey)，並點下create API
   ![螢幕擷取畫面 2025-06-02 203828](https://github.com/user-attachments/assets/04cdc7be-0121-4b72-b801-9c83e4f91e29)
2. 複製API KEY
   
  ![螢幕擷取畫面 2025-06-02 204040](https://github.com/user-attachments/assets/920d3ba3-c6a6-4316-93f3-43043440e9c1)

3. 貼到`.env`中的GEMINI_API ="**在這裡貼上您的API KEY**"
   
  請不要隨意洩漏您的API，這相當於忘記登出的GMAIL帳號，任何人都可以使用



### SERPAPI_API_KEY
1. 前往[SerpAPI](https://serpapi.com/)，如果你是第一次來請註冊，驗證手機與電子郵件
   
2. 登錄並複製
   
   ![螢幕擷取畫面 2025-06-02 205248](https://github.com/user-attachments/assets/b6ed269c-f804-4aa1-8144-db0d2f7b2117)
   
3. 貼到`.env`中的SERPAPI_API_KEY ="**在這裡貼上您的Your Private API Key**"
  請不要隨意洩漏您的api



### GOOGLE_MAPS_API
開始前提醒您，為了激活90天免費試用，您需要一張信用卡用於註冊
1. 前往[Google Cloud Console](https://console.cloud.google.com/apis/dashboard)
2. 隨便選一個project(可能有Gemini API)
   
  ![螢幕擷取畫面 2025-06-02 210153](https://github.com/user-attachments/assets/33e35a48-6ab3-41cc-9b36-7f6960f77848)

3. 激活Directions api
   
   ![螢幕擷取畫面 2025-06-02 210503](https://github.com/user-attachments/assets/4f08f15d-e8bc-477d-9d1c-c509e0550b5b)
   
   ![螢幕擷取畫面 2025-06-02 210642](https://github.com/user-attachments/assets/268c1b0c-bf05-4f59-a144-a26e860c92df)
   
4. 創建api key
   
   ![螢幕擷取畫面 2025-06-02 210906](https://github.com/user-attachments/assets/c041a638-208a-4e2a-bacc-046b39e40cf4)
   
5. 創建完成後請點擊右側的edited api key
   
   ![螢幕擷取畫面 2025-06-02 211211](https://github.com/user-attachments/assets/af1d3853-2caf-45ba-9f3e-2c35ef3bc060)
   
6. 將API restrictions 切換成Restrict key並勾選Directions api，最後記得按下保存。
   
   ![螢幕擷取畫面 2025-06-02 211354](https://github.com/user-attachments/assets/4ef2fb38-410e-4a84-a71c-737a483e0b71)
   
   ![螢幕擷取畫面 2025-06-02 211450](https://github.com/user-attachments/assets/ea60e6dd-2ea6-43ca-82fc-7958b935533f)
   
8. 點擊show key，並複製粘貼到`.env`中的GOOGLE_MAPS_API ="**在這裡貼上您的API KEY**"
   
    ![螢幕擷取畫面 2025-06-02 214408](https://github.com/user-attachments/assets/2ba93e86-be76-4ce0-9abf-d81058b6a4b5)



### NASA_API

1. 前往[NASA API](https://api.nasa.gov/)，點選get start
2. 誠實填寫您的電子郵件，之後api就會被發送到您的信箱了
3. 複製粘貼到`.env`中的NASA_API ="**在這裡貼上您的NASA API KEY**"


## 執行

1. 在TERMINAL中輸入以下指令
   
    ```bash
    python main.py
    ```
    
2. 如果成功執行terminal 上會有如下輸出

  ![螢幕擷取畫面 2025-06-02 212454](https://github.com/user-attachments/assets/9bdd9672-bf0f-4764-b8af-54bdd303a260)

3. 可以去discord 中測試機器人了喔!!

