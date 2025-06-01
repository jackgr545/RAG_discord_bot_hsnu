
import os

from dotenv import load_dotenv
from rag_engine import build_prompt
from serpapi import GoogleSearch
import google.generativeai as genai
# 為方便管理，將TOKEN寫在.env檔案裡，並用dotenv調用
load_dotenv()

SERP_API_KEY = os.getenv("SERPAPI_API_KEY")
GEMINI_API_KEY =os.getenv("GEMINI_API")


# 設定 API 金鑰
genai.configure(api_key=GEMINI_API_KEY)

# 設定模型
model = genai.GenerativeModel("gemini-2.0-flash")
    #user_input 爲使用者輸入
def generate(user_input,chat_history,mode,t):
    try:
        #prompt用來存放最後要交給ai的prompt
        prompt ="你是附中專家，請根據以下幾點資訊用繁體中文回答使用者的問題，並請不要回答任何與附中無關的問題，無論何時何地何種理由:\n\n"
        #加入記憶
        if chat_history :
            prompt += f"\n1.這是使用者與你對話的紀錄:\n{chat_history}\n"
        #如果開啟搜尋功能，則加入google的搜尋結果
        if mode == "google_search" :
            #讓搜尋的事物與師大附中有關
            target=f"師大附中，{user_input}"
            summary =summarize_search(target)
            prompt += f"\n2.這是 google 搜尋結果：{summary}\n"
        if mode == "just_RAG":
            #加入RAG採集到的資料
            prompt += build_prompt(user_input)
        if mode =="nasa_apod" :
            prompt =f"請根據以下資料，用繁體中文對整張照片作出解釋，並請忽略url與hdurl:\n"
            prompt +=f"{str(user_input)}\n"
            #user_input的樣子
            """{
            "copyright": "\nDomingo Pestana\n",
            "date": "2025-06-01",
            "explanation": "What's happening to this spiral galaxy? Although details remain uncertain, it surely has to do with an ongoing battle with its smaller galactic neighbor. The featured galaxy is labelled UGC 1810 by itself, but together with its collisional partner is known as Arp 273. The overall shape of UGC 1810 -- in particular its blue outer ring -- is likely a result of wild and violent gravitational interactions. This ring's blue color is caused by massive stars that are blue hot and have formed only in the past few million years.  The inner galaxy appears older, redder, and threaded with cool filamentary dust.  A few bright stars appear well in the foreground, unrelated to UGC 1810, while several galaxies are visible well in the background.  Arp 273 lies about 300 million light years away toward the constellation of Andromeda.  Quite likely, UGC 1810 will devour its galactic sidekick over the next billion years and settle into a classic spiral form.",
            "hdurl": "https://apod.nasa.gov/apod/image/2506/Arp273Main_HubblePestana_3079.jpg",
            "media_type": "image",
            "service_version": "v1",
            "title": "UGC 1810: Wildly Interacting Galaxy from Hubble",
            "url": "https://apod.nasa.gov/apod/image/2506/Arp273Main_HubblePestana_1080.jpg"
            }"""
        #觀察AI拿到的資料    
        print(f"\n--------------------------以下為第{t+1}輪對話--------------------------\n輸入:\n{prompt}")
        # 產生回應（串流方式）
        response = model.generate_content(prompt, stream=True)

        # 輸出回應
        response_text = ""
        for chunk in response:
            print(chunk.text, end="", flush=True)
            response_text += chunk.text
    
        return response_text

    except Exception as e:
        print(f"\n❌ 錯誤：{e}")

        
def search_google(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERP_API_KEY
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return results.get("organic_results", [])


def summarize_search(query):
    results = search_google(query)
    if not results:
        return "沒有找到任何搜尋結果"

    content = ""
    for i, res in enumerate(results[:3]):  # 取前3筆
        title = res.get("title", "")
        snippet = res.get("snippet", "")
        content += f"{i+1}. {title}\n{snippet}\n\n"

    prompt = f"以下是我對『{query}』的搜尋結果，請幫我整理重點並總結分析：\n{content}"
    response = model.generate_content(prompt)
    return response.text

