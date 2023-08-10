import random
import json
import discord
from discord import app_commands
from discord.ext import commands
from pathlib import Path

import os

class Randomazzo():
    def __init__(self) -> None:
        pass
        
    def get_flavor_array(self, flavor_type):
        json_filepath = str(Path(os.path.dirname(__file__)).parents[0]) + "/_json/flavor.json"
        
        with open(json_filepath) as f:
            data = json.load(f)
            flavor_text_array = random.choice(data[flavor_type])
            return flavor_text_array
            
    def get_img(self, img_name):
        img_filepath = str(Path(os.path.dirname(__file__)).parents[0]) + f"/_img/{img_name}"
        file = discord.File(img_filepath, filename = "image.png")
        return file
        
    async def make_embed(self, flavor_type, title, interaction, desc: str = None, footer: str = None):
        embed_array = self.get_flavor_array(flavor_type)
        embed_title = title
        embed_desc = desc if desc else embed_array["desc"]
        embed_footer = footer if footer else embed_array["footer"]
        file = self.get_img(embed_array["img"])
        embed = discord.Embed(title = embed_title, description = embed_desc)
        embed.set_thumbnail(url="attachment://image.png")
        embed.set_footer(text = embed_footer)
        await interaction.response.send_message(file = file, embed = embed)