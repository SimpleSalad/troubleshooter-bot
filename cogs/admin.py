import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

@app_commands.check(is_owner)
@app_commands.command(name = "shutdown", description = "Shuts down the bot.")
async def shutdown(self, interaction: discord.Interaction):
    embed = discord.Embed(title = "", description = "Incredible!")
    message = interaction.message
    await interaction.response.send_message(embed = embed)
    
    print("\nShutdown by command.")
    await self.bot.close()