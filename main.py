import discord
import os
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from generate_response import generate
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
    global chat_history
    global t 
    # 呼叫 Gemini  API，添加RAG的資料
    result =  generate(text,chat_history,mode="just_RAG",t=t)
    t+=1
    chat_history +=f"第{t}次的使用者輸入:{text}\n"
    chat_history +=f"對第{t}次使用者的回覆:{result}\n"
    await interaction.followup.send(f"AI 回答：{result}", ephemeral=True)

@bot.tree.command(name= "google_search",description= "允許ai使用google來搜尋資料", guild=GUILD_ID)
@app_commands.describe(text="ex:附中工研的社團代號？")
async def googole_search(interaction: discord.Interaction, text: str):
    # 回覆私密訊息
    await interaction.response.defer(ephemeral=True)  # 告訴 Discord「我在處理中」
    global chat_history
    global t 
    # 呼叫 Gemini  API ，添加RAG&GOOGLE的資料進入PROMPT
    result =  generate(text,chat_history,mode="google_search",t=t)
    t+=1
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