import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice
import requests
import typing
import json

from io import StringIO

from cogs.utils.randomazzo import make_embed

import os
import json
import asyncio

class DFO(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sauce = bot.secret_sauce("DFO_KEY")
    
    dfo = app_commands.Group(name = "dfo", description = "DFO related commands.")
    
    def __get_char(self, server_id, char_name):
        req = f"https://api.dfoneople.com/df/servers/{server_id}/characters?characterName={char_name}&limit=1&apikey={self.sauce}"
        response = requests.get(req).json()
        return response
    
    def __get_char_equips(self, server_id, char_id):
        req = f"https://api.dfoneople.com/df/servers/{server_id}/characters/{char_id}/equip/equipment?apikey={self.sauce}"
        response = requests.get(req).json()
        return response
    
    @dfo.command(name = "char", description = "Returns given character's equipment.")
    @app_commands.describe(name = "Character Name")
    async def char(self, interaction: discord.Interaction, name: str, server: typing.Literal["cain", "sirocco", "all"] = "all"):
        response = self.__get_char(server, name)
        if not response or "error" in response or not response["rows"]:
            if server == "all":
                error = f"Character `{name}` not found!"
                await make_embed(flavor_type = "error", title = "Error!", interaction = interaction, desc = error)
            if server != "all":
                error = f"Character `{name}` not found on server `{server}`!"
                await make_embed(flavor_type = "error", title = "Error!", interaction = interaction, desc = error)
        response = response["rows"][0]
        char_id = response["characterId"]
        server_id = response["serverId"]
        equips = self.__get_char_equips(server_id, char_id)
        file = StringIO()
        file.write(json.dumps(equips))
        file.seek(0)
        await interaction.response.send_message(file = discord.File(fp = file, filename = f"{name}.json"))
        file.close()
    

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(DFO(bot))