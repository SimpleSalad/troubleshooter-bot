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
        
        await self.bot.tree.sync()
        
        await Randomazzo().make_embed(flavor_type = "sync", title = "Commands synced.", interaction = interaction)
        
    @app_commands.check(is_owner)
    @app_commands.command(name = "clearcommands", description = "Clears commands.")
    async def clear_commands(self, interaction: discord.Interaction):

        self.bot.tree.clear_commands(guild = interaction.guild)
        await self.bot.tree.sync()
        
        await Randomazzo().make_embed(flavor_type = "sync", title = "Commands cleared.", interaction = interaction)
        
    
    @app_commands.check(is_owner)
    @app_commands.command(name = "shutdown", description = "Stops the bot.")
    async def shutdown(self, interaction: discord.Interaction):
        await Randomazzo().make_embed(flavor_type = "boom", title = "Shutting down.", interaction = interaction)
        print("\nShutdown by command.")
        await self.bot.close()

    @app_commands.check(is_owner)
    @app_commands.command(name = "reload", description = "Reload a cog.")
    @app_commands.choices(cog = [Choice(name = str(cog_name), value = value) for (value, cog_name) in enumerate(os.listdir("cogs"), 1) if cog_name.endswith(".py")])
    async def reload(self, interaction: discord.Interaction, cog: Choice[int]):
        try:
          await self.bot.reload_extension("cogs." + cog.name[:-3])
        except Exception as error:
            await Randomazzo().make_embed(flavor_type = "error", title = "Error!", interaction = interaction, desc = error)
        else:
            await Randomazzo().make_embed(flavor_type = "reload", title = f"`{cog.name}` reloaded.", interaction = interaction)
            
    @app_commands.check(is_owner)
    @app_commands.command(name = "unload", description = "Unload a cog.")
    @app_commands.choices(cog = [Choice(name = str(cog_name), value = value) for (value, cog_name) in enumerate(os.listdir("cogs"), 1) if cog_name.endswith(".py") and cog_name != "admin.py"])
    async def unload(self, interaction: discord.Interaction, cog: Choice[int]):
        try:
          await self.bot.unload_extension("cogs." + cog.name[:-3])
        except Exception as error:
            await Randomazzo().make_embed(flavor_type = "error", title = "Error!", interaction = interaction, desc = error)
        else:
            await Randomazzo().make_embed(flavor_type = "reload", title = f"`{cog.name}` unloaded.", interaction = interaction)
    
    @app_commands.check(is_owner)
    @app_commands.command(name = "load", description = "Load a cog.")
    @app_commands.choices(cog = [Choice(name = str(cog_name), value = value) for (value, cog_name) in enumerate(os.listdir("cogs"), 1) if cog_name.endswith(".py") and cog_name != "admin.py"])
    async def load(self, interaction: discord.Interaction, cog: Choice[int]):
        try:
          await self.bot.load_extension("cogs." + cog.name[:-3])
        except Exception as error:
            await Randomazzo().make_embed(flavor_type = "error", title = "Error!", interaction = interaction, desc = error)
        else:
            await Randomazzo().make_embed(flavor_type = "reload", title = f"`{cog.name}` loaded.", interaction = interaction)

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Admin(bot))