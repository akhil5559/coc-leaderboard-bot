import discord
from discord.ext import commands
from database import get_leaderboard_data, save_leaderboard_data

class Remove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="remove", help="Admin: Remove any player from leaderboard")
    @commands.has_permissions(administrator=True)
    async def remove(self, ctx, tag: str):
        leaderboard_data = get_leaderboard_data()
        tag = tag.upper().replace("#", "")

        if tag not in leaderboard_data:
            return await ctx.send(f"⚠️ Account `#{tag}` is not in leaderboard.")

        del leaderboard_data[tag]
        save_leaderboard_data()

        await ctx.send(f"✅ Account `#{tag}` removed from leaderboard!")

async def setup(bot):
    await bot.add_cog(Remove(bot))