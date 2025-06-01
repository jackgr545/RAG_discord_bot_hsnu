import discord
import os
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from generate_response import generate
from datetime import datetime
from nasa import apod
# 為方便管理，將TOKEN寫在.env檔案裡，並用dotenv調用
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER_ID = int(os.getenv("DISCORD_SERVER_ID"))
GUILD_ID = discord.Object(id=SERVER_ID)

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
@app_commands.describe(user_input="ex:舊北在哪裏？附中怪鳥是什麼？")
async def ask(interaction: discord.Interaction, user_input: str):
    
    
    # 回覆私密訊息
    await interaction.response.defer(ephemeral=True)  # 告訴 Discord「我在處理中」
    global chat_history
    global t 
    # 呼叫 Gemini  API，添加RAG的資料
    result =  generate(user_input=user_input,chat_history=chat_history,mode="just_RAG",t=t)
    t+=1
    chat_history +=f"第{t}次的使用者輸入:{user_input}\n"
    chat_history +=f"對第{t}次使用者的回覆:{result}\n"
    await interaction.followup.send(f"AI 回答：{result}", ephemeral=True)

@bot.tree.command(name= "google_search",description= "允許ai使用google來搜尋資料", guild=GUILD_ID)
@app_commands.describe(user_input="ex:附中工研的社團代號？")
async def googole_search(interaction: discord.Interaction, user_input: str):
    # 回覆私密訊息
    await interaction.response.defer(ephemeral=True)  # 告訴 Discord「我在處理中」
    global chat_history
    global t 
    # 呼叫 Gemini  API ，添GOOGLE的資料進入PROMPT
    result =  generate(user_input=user_input,chat_history=chat_history,mode="google_search",t=t)
    t+=1
    chat_history +=f"第{t}次的使用者輸入:{user_input}\n"
    chat_history +=f"對第{t}次使用者的回覆:{result}\n"
    await interaction.followup.send(f"AI 回答：{result}", ephemeral=True)

"""
@bot.tree.command(name="google_map",description="提供你的位置以及你想去的地方",guild=GUILD_ID)
@app_commands.describe(text ="因爲discord無法直接取得您的位置，故需要您手動輸入")
async def google_map(interaction: discord.Interaction, 目前位置: str,想去之地 :str):
    await interaction.response.defer(ephemeral=True)
""" 
@bot.tree.command(name="apod",description="nasa提供的每日照片",guild=GUILD_ID)
@app_commands.describe(date = "提供一個日期，ex:2025-06-01")
async def nasa_picture(interaction :discord.Interaction, date :str):
    await interaction.response.defer(ephemeral=True)
    try:
        # 嘗試解析使用者輸入的日期
        parsed_date = datetime.strptime(date, "%Y-%m-%d").date()
        # 在此處加入呼叫 NASA API 的邏輯，使用 parsed_date
        global chat_history
        global t 
        data_json =apod(parsed_date)
        output =generate(user_input=data_json,chat_history="",mode="nasa_apod",t=t)
        t+= 1
        chat_history +=f"第{t}次的使用者輸入:{date}\n"
        chat_history +=f"對第{t}次使用者的回覆:{output}\n"
        await interaction.followup.send(f"AI的回答:{output}\n網址:{str(data_json['hdurl'])}",ephemeral=True)
        
    except ValueError:
        # 如果解析失敗，提示使用者輸入正確的格式
        await interaction.followup.send("請輸入正確的日期格式，例如：YYYY-MM-DD",ephemeral=True)
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