import random
import json
import discord
from pathlib import Path

import os
 
def get_flavor_array(flavor_type):
    json_filepath = str(Path(os.path.dirname(__file__)).parents[0]) + "/_json/flavor.json"
    
    with open(json_filepath) as f:
        data = json.load(f)
        flavor_text_array = random.choice(data[flavor_type])
        return flavor_text_array
        
def get_img(img_name):
    img_filepath = str(Path(os.path.dirname(__file__)).parents[0]) + f"/_img/{img_name}"
    file = discord.File(img_filepath, filename = "image.png")
    return file
    
async def make_embed(flavor_type, title, interaction, desc: str = None, footer: str = None):
    embed_array = get_flavor_array(flavor_type)
    embed_title = title
    embed_desc = desc if desc else embed_array["desc"]
    embed_footer = footer if footer else embed_array["footer"]
    file = get_img(embed_array["img"])
    embed = discord.Embed(title = embed_title, description = embed_desc)
    embed.set_thumbnail(url="attachment://image.png")
    embed.set_footer(text = embed_footer)
    await interaction.response.send_message(file = file, embed = embed)

async def make_error(title, interaction, desc: str = None):
    await make_embed(flavor_type = "error", title = title, interaction = interaction, desc = desc)