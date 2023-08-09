import discord
from discord import app_commands
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def is_owner(interaction: discord.Interaction) -> bool:
        return interaction.user.id == 88087496189022208
    
    @app_commands.check(is_owner)
    @app_commands.command(name = "shutdown", description = "Stops the bot.")
    async def shutdown(self, interaction: discord.Interaction):
        embed = discord.Embed(title = "Shutting down.", description = "이건 몰랐을걸? Incredible!")
        message = interaction.message
        await interaction.response.send_message(embed = embed)
    
        print("\nShutdown by command.")
        await self.bot.close()

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Admin(bot))