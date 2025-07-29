import discord, os
from discord.ext import commands, tasks
from database import get_leaderboard_data, save_leaderboard_data

TOKEN = os.getenv("DISCORD_TOKEN")  # Replit secrets

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Load all command files
@bot.event
async def setup_hook():
    for file in os.listdir("commands"):
        if file.endswith(".py"):
            await bot.load_extension(f"commands.{file[:-3]}")
    print("✅ All command files loaded")

@bot.event
async def on_ready():
    print(f"🤖 Logged in as {bot.user}")
    auto_refresh_leaderboard.start()

# Auto refresh leaderboard every 1 min
@tasks.loop(minutes=1)
async def auto_refresh_leaderboard():
    leaderboard_data = get_leaderboard_data()
    # Later: Fetch Clash API, update trophies, reset daily offence/defense at 10:30 IST
    save_leaderboard_data()

bot.run(TOKEN)