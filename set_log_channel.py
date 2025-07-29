import discord
from discord.ext import commands

class SetLogChannel(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.log_channel_id = None

    @commands.command(name="set_log_channel", help="Admin: Set log channel for bot events")
    @commands.has_permissions(administrator=True)
    async def set_log_channel(self, ctx, channel: discord.TextChannel):
        self.log_channel_id = channel.id
        await ctx.send(f"✅ Log channel set to {channel.mention}")

async def setup(bot):
    await bot.add_cog(SetLogChannel(bot))