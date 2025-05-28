import discord
import os
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from rag_engine import build_prompt
from serpapi import GoogleSearch
import google.generativeai as genai
# 為方便管理，將TOKEN寫在.env檔案裡，並用dotenv調用
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER_ID = int(os.getenv("DISCORD_SERVER_ID"))
GUILD_ID = discord.Object(id=SERVER_ID)
SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")
"""變數的資料儲存與記憶體中，會在檔案從啓時清除"""
#宣告全域變數
#chat_history用來存放對話記錄
chat_history = ""
#用來記錄對話次數
t = 0 

# 設定 API 金鑰
genai.configure(api_key=os.getenv("GEMINI_API"))

# 設定模型
model = genai.GenerativeModel("gemini-2.0-flash")
    #prompt 爲使用者輸入
def generate(prompt):
    try:
        #user_input用來存放最後要交給ai的prompt
        user_input = ""
        global chat_history 
        #如果有聊天歷史記錄，將其加入要交給ai的prompt
        if   chat_history :
            user_input+=f"這是使用者與你對話的紀錄:\n{chat_history}\n"
        #加入RAG採集到的資料
        user_input += build_prompt(prompt)
        
        #觀察AI拿到的資料    
        print(f"{user_input}\n---------------------------分隔線---------------------------\n")
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

def generate_with_google_search(prompt):
    try:
        #user_input用來存放最後要交給ai的prompt
        user_input = ""
        global chat_history 
        #如果有聊天歷史記錄，將其加入要交給ai的prompt
        if   chat_history :
            user_input+=f"這是使用者與你對話的紀錄:\n{chat_history}\n"
        #加入google的搜尋結果
        user_input += f"google 搜尋結果：{summarize_search(search_google(prompt))}\n"
        #加入RAG採集到的資料
        user_input += build_prompt(prompt)
        #觀察AI拿到的資料    
        print(f"{user_input}\n---------------------------分隔線---------------------------\n")
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

# 創建許可權物件
intents = discord.Intents.default()
# 接發訊息權限
intents.message_content = True
# 添加語音相關權限
intents.voice_states = True
intents.guilds = True
# 創建機器人實例
bot = commands.Bot(command_prefix="!", intents=intents)

# 創建一個/命令 叫/ask
@bot.tree.command(name="ask", description="關於附中你有什麼想問的問題", guild=GUILD_ID)
@app_commands.describe(text="ex:舊北在哪裏？附中怪鳥是什麼？")
async def ask(interaction: discord.Interaction, text: str):
    
    
    # 回覆私密訊息
    await interaction.response.defer(ephemeral=True)  # 告訴 Discord「我在處理中」

    # 呼叫 Gemini  API
    result =  generate(text)
    global t 
    t+=1
    global chat_history
    chat_history +=f"第{t}次的使用者輸入:{text}\n"
    chat_history +=f"對第{t}次使用者的回覆:{result}\n"
    await interaction.followup.send(f"AI 回答：{result}", ephemeral=True)

@bot.tree.command(name= "google_search",description= "允許ai使用google來搜尋資料", guild=GUILD_ID)
@app_commands.describe(text="ex:附中工研的社團代號？")
async def googole_search(interaction: discord.Interaction, text: str):
    # 回覆私密訊息
    await interaction.response.defer(ephemeral=True)  # 告訴 Discord「我在處理中」

    # 呼叫 Gemini  API
    result =  generate_with_google_search(text)
    global t 
    t+=1
    global chat_history
    chat_history +=f"第{t}次的使用者輸入:{text}\n"
    chat_history +=f"對第{t}次使用者的回覆:{result}\n"
    await interaction.followup.send(f"AI 回答：{result}", ephemeral=True)




# 當機器人上線時執行
@bot.event 
async def on_ready():
    try:
       
        # 同步指令
        synced = await bot.tree.sync(guild=GUILD_ID)
        print(f"✅ 已同步 {len(synced)} 個指令到 Guild {GUILD_ID}")
        
        # 檢查同步後的指令
        commands = await bot.tree.fetch_commands(guild=GUILD_ID)
        if commands:
            for cmd in commands:
                print(f"📌 已同步指令：/{cmd.name}")
        else:
            print("⚠️ 警告：同步後沒有指令")
            
        
            
    except Exception as e:
        print(f"❌ 同步失敗: {e}")
        
    print(f"🤖 機器人已登入為 {bot.user}")
def run_bot ():
    bot.run(TOKEN)
run_bot()