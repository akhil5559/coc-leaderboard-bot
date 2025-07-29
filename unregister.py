import discord
from discord.ext import commands
from database import get_leaderboard_data, save_leaderboard_data, get_player_data

class Unregister(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="unregister", help="Remove your account from leaderboard")
    async def unregister(self, ctx):
        user_id = str(ctx.author.id)
        players_data = get_player_data()
        leaderboard_data = get_leaderboard_data()

        # Show only accounts user has linked and are registered
        if user_id not in players_data:
            return await ctx.send("⚠️ You have no linked accounts.")

        registered_tags = [tag for tag in players_data[user_id]["linked_accounts"] if tag in leaderboard_data]

        if not registered_tags:
            return await ctx.send("⚠️ You have no registered accounts.")

        options = [discord.SelectOption(label=tag, value=tag) for tag in registered_tags]

        select = discord.ui.Select(placeholder="Select account to unregister", options=options)

        async def select_callback(interaction: discord.Interaction):
            tag = select.values[0]
            del leaderboard_data[tag]
            save_leaderboard_data()

            await interaction.response.send_message(f"✅ Account `#{tag}` removed from leaderboard!", ephemeral=True)

        select.callback = select_callback
        view = discord.ui.View()
        view.add_item(select)

        await ctx.send("🔽 Select an account to remove:", view=view)

async def setup(bot):
    await bot.add_cog(Unregister(bot))