import discord
from discord.ext import commands
from database import get_player_data, save_player_data

class Unlink(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="unlink", help="Unlink your Clash of Clans account")
    async def unlink(self, ctx, tag: str):
        user_id = str(ctx.author.id)
        tag = tag.upper().replace("#", "")

        players_data = get_player_data()

        if user_id not in players_data or tag not in players_data[user_id]["linked_accounts"]:
            return await ctx.send(f"⚠️ Account `#{tag}` is not linked with you.")

        players_data[user_id]["linked_accounts"].remove(tag)
        save_player_data()

        await ctx.send(f"✅ Account `#{tag}` has been unlinked!")

async def setup(bot):
    await bot.add_cog(Unlink(bot))