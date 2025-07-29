import discord, datetime
from discord.ext import commands
from database import get_leaderboard_data

class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="leaderboard")
    @commands.has_permissions(administrator=True)
    async def leaderboard(self, ctx, *, leaderboard_name="Leaderboard", color="#000000"):
        leaderboard_data = get_leaderboard_data()

        if not leaderboard_data:
            return await ctx.send("⚠️ No players registered in leaderboard!")

        sorted_players = sorted(leaderboard_data.values(), key=lambda x: x["trophies"], reverse=True)

        # Pagination - 15 players per page
        pages = []
        page_data = []
        for idx, player in enumerate(sorted_players, start=1):
            offence = player.get("offence", "+0/0")
            defence = player.get("defence", "-0/0")
            line = f"**{idx}. {player['name']}** ({player['tag']})\n🏆 {player['trophies']} | ⚔️ {offence} | 🛡️ {defence}"
            page_data.append(line)

            if len(page_data) == 15 or idx == len(sorted_players):
                pages.append("\n\n".join(page_data))
                page_data = []

        embeds = []
        for i, page in enumerate(pages):
            embed = discord.Embed(
                title=leaderboard_name,
                description=page,
                color=int(color.strip("#"), 16)
            )
            refresh_time = datetime.datetime.now().strftime('%I:%M %p')
            embed.set_footer(text=f"Page {i+1}/{len(pages)} • Last refresh: {refresh_time}")
            embeds.append(embed)

        message = await ctx.send(embed=embeds[0])

        if len(embeds) > 1:
            await message.add_reaction("⬅️")
            await message.add_reaction("➡️")

async def setup(bot):
    await bot.add_cog(Leaderboard(bot))