import discord
import os
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
from rag_engine import build_prompt

import google.generativeai as genai
# 為方便管理，將TOKEN寫在.env檔案裡，並用dotenv調用
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
SERVER_ID = int(os.getenv("DISCORD_SERVER_ID"))
GUILD_ID = discord.Object(id=SERVER_ID)
# 設定 API 金鑰
genai.configure(api_key=os.getenv("GEMINI_API"))

# 建立模型
model = genai.GenerativeModel("gemini-2.0-flash")
def generate(prompt):
    try:
        # 取得使用者輸入
         
        user_input = build_prompt(prompt)
        #觀察AI拿到的資料    
        print(f"{user_input}")
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



# 創建許可權物件
intents = discord.Intents.default()
# 接發訊息權限
intents.message_content = True
# 添加語音相關權限
intents.voice_states = True
intents.guilds = True
# 創建機器人實例
bot = commands.Bot(command_prefix="!", intents=intents)

# 創建一個/命令 叫/describe
@bot.tree.command(name="ask", description="關於附中你有什麼想問的問題", guild=GUILD_ID)
@app_commands.describe(text="ex:舊北在哪裏？附中怪鳥是什麼？")
async def describe(interaction: discord.Interaction, text: str):
    
    
    # 回覆私密訊息
    await interaction.response.defer(ephemeral=True)  # 告訴 Discord「我在處理中」

    # 呼叫 Gemini  API
    result =  generate(text)
    
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