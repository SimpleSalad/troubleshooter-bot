import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

from typing import Literal
import os
import json
import asyncio

from cogs.utils.randomazzo import Randomazzo


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def is_owner(interaction: discord.Interaction) -> bool:
        return interaction.user.id == 88087496189022208
        
    @app_commands.check(is_owner)
    @app_commands.command(name = "sync", description = "Synchronizes commands.")
    async def sync(self, interaction: discord.Interaction):
        embed = discord.Embed(title = "Commands synced.", description = "가 볼까?")
        embed.set_thumbnail(url='https://wiki.dfo-world.com/images/4/43/Swashbuckler%27s_Refreshment.png')
        embed.set_footer(text = "Shall we go?")
        await self.bot.tree.sync()
        await interaction.response.send_message(embed = embed)
        
    @app_commands.check(is_owner)
    @app_commands.command(name = "clearcommands", description = "Clears commands.")
    async def clear_commands(self, interaction: discord.Interaction):
        embed = discord.Embed(title = "Commands cleared.", description = "가 볼까?")
        embed.set_thumbnail(url='https://wiki.dfo-world.com/images/4/43/Swashbuckler%27s_Refreshment.png')
        embed.set_footer(text = "Shall we go?")
        self.bot.tree.clear_commands(guild = None)
        await self.bot.tree.sync()
        await interaction.response.send_message(embed = embed)
        
    
    @app_commands.check(is_owner)
    @app_commands.command(name = "shutdown", description = "Stops the bot.")
    async def shutdown(self, interaction: discord.Interaction):
        flavor = Randomazzo("boom").get_flavor()
        file = discord.File(os.path.dirname(__file__) + "/_img/" + flavor.img, filename = "image.png")
        embed = discord.Embed(title = "Shutting down.", description = flavor.desc)
        embed.set_thumbnail(url="attachment://image.png")
        embed.set_footer(text = flavor.footer)
        await interaction.response.send_message(file = file, embed = embed)
    
        print("\nShutdown by command.")
        await self.bot.close()

    @app_commands.check(is_owner)
    @app_commands.command(name = "reload", description = "Reload a cog.")
    @app_commands.choices(cog = [Choice(name = str(cog_name), value = value) for (value, cog_name) in enumerate(os.listdir("cogs"), 1) if cog_name.endswith(".py")])
    async def reload(self, interaction: discord.Interaction, cog: Choice[int]):
        try:
          await self.bot.reload_extension("cogs." + cog.name[:-3])
        except Exception as error:
            embed = self.bot.create_error_response(error = error)
        else:
            embed = discord.Embed(title = f"`{cog.name}` reloaded.", description = "가 볼까?")
            embed.set_thumbnail(url='https://wiki.dfo-world.com/images/4/43/Swashbuckler%27s_Refreshment.png')
            embed.set_footer(text = "Shall we go?")
        await interaction.response.send_message(embed = embed)

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Admin(bot))