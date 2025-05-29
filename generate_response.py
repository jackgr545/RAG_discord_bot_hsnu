
import os

from dotenv import load_dotenv
from rag_engine import build_prompt
from serpapi import GoogleSearch
import google.generativeai as genai
# 為方便管理，將TOKEN寫在.env檔案裡，並用dotenv調用
load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")



# 設定 API 金鑰
genai.configure(api_key=os.getenv("GEMINI_API"))

# 設定模型
model = genai.GenerativeModel("gemini-2.0-flash")
    #prompt 爲使用者輸入
def generate(prompt,chat_history,mode,t):
    try:
        #user_input用來存放最後要交給ai的prompt
        user_input ="你是附中專家，請根據以下幾點資訊用繁體中文回答使用者的問題，並請不要回答任何與附中無關的問題，無論何時何地何種理由:\n\n"
        #加入記憶
        if chat_history :
            user_input += f"\n1.這是使用者與你對話的紀錄:\n{chat_history}\n"
        #如果開啟搜尋功能，則加入google的搜尋結果
        if mode == "google_search" :
            #讓搜尋的事物與師大附中有關
            target=f"師大附中，{prompt}"
            summary =summarize_search(target)
            user_input += f"\n2.這是 google 搜尋結果：{summary}\n"
        #加入RAG採集到的資料
        user_input += build_prompt(prompt)
        
        #觀察AI拿到的資料    
        print(f"\n--------------------------以下為第{t+1}輪對話--------------------------\n輸入:\n{user_input}")
        # 產生回應（串流方式）
        response = model.generate_content(user_input, stream=True)

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
        "api_key": SERPAPI_KEY
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

