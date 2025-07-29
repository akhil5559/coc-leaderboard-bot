import discord
from discord.ext import commands
from database import get_player_data, get_leaderboard_data, save_leaderboard_data

class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="register", help="Register your linked account to leaderboard")
    async def register(self, ctx):
        user_id = str(ctx.author.id)
        players_data = get_player_data()
        leaderboard_data = get_leaderboard_data()

        # Check linked accounts
        if user_id not in players_data or not players_data[user_id]["linked_accounts"]:
            return await ctx.send("⚠️ You have no linked accounts! Use `!link` first.")

        linked_accounts = players_data[user_id]["linked_accounts"]

        # Show dropdown menu
        options = [discord.SelectOption(label=tag, value=tag) for tag in linked_accounts]

        select = discord.ui.Select(placeholder="Select account to register", options=options)

        async def select_callback(interaction: discord.Interaction):
            tag = select.values[0]

            if tag in leaderboard_data:
                await interaction.response.send_message(f"⚠️ Account `#{tag}` is already registered!", ephemeral=True)
                return

            leaderboard_data[tag] = {
                "tag": tag,
                "name": f"Player-{tag}",   # Later replace with API fetched IGN
                "trophies": 0,
                "offence": "+0/0",
                "defence": "-0/0"
            }
            save_leaderboard_data()

            await interaction.response.send_message(f"✅ Account `#{tag}` registered to leaderboard!", ephemeral=True)

        select.callback = select_callback
        view = discord.ui.View()
        view.add_item(select)

        await ctx.send("🔽 Select an account to register:", view=view)

async def setup(bot):
    await bot.add_cog(Register(bot))