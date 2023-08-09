import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice

from typing import Literal
import os
import json
import asyncio

class Dfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def is_owner(interaction: discord.Interaction) -> bool:
        return interaction.user.id == 88087496189022208

async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Dfo(bot))