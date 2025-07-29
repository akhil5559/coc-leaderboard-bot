import discord, re
from discord.ext import commands
from database import get_player_data, save_player_data

class Link(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="link", help="Link your Clash of Clans account using player tag")
    async def link(self, ctx, tag: str):
        tag = tag.upper().replace("#", "")

        if not re.match(r"^[0289PYLQGRJCUV]{5,15}$", tag):
            return await ctx.send("⚠️ Invalid player tag. Please enter a valid tag.")

        players_data = get_player_data()
        user_id = str(ctx.author.id)

        if user_id not in players_data:
            players_data[user_id] = {"linked_accounts": []}

        if tag in players_data[user_id]["linked_accounts"]:
            return await ctx.send("⚠️ This account is already linked.")

        players_data[user_id]["linked_accounts"].append(tag)
        save_player_data()

        await ctx.send(f"✅ Your account `#{tag}` has been linked!")

async def setup(bot):
    await bot.add_cog(Link(bot))