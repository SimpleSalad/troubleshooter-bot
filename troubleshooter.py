from os.path import dirname, basename, isfile
import os
import sys
import importlib
import discord
import asyncio
import socket

from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands

load_dotenv()

HOST = '0.0.0.0'
PORT = 8080

class troubleshooter(commands.Bot):
    def __init__(self) -> None:
        intents = discord.Intents.all()
        command_prefix = "fn$"
        super().__init__(command_prefix = command_prefix,
                         intents = intents,
                         owner_id = 88087496189022208,
                         status = discord.Status.do_not_disturb,
                         activity = discord.Game(name = "Dungeon Fighter Online", type = discord.ActivityType.custom))
                         
    def secret_sauce(self, sauce_type):
        return os.getenv(sauce_type)
        
    def generic_error(self, error):
        embed = discord.Embed(title = "Error!", description = error)
        return embed

    async def setup_hook(self):
        imported_cogs = 0
        total_cogs = 0
        
        cogs = os.path.join(os.path.dirname(__file__), 'cogs/')
        for cog in os.listdir(cogs):
            cog_name = os.fsdecode(cog)
            if cog_name != "__init__.py" and cog_name.endswith(".py"):
                total_cogs += 1
                try:
                    await self.load_extension(f"cogs.{cog_name[:-3]}")
                    imported_cogs += 1
                except Exception as error:
                    print(f"X: {cog_name} could not be loaded ({type(error).__name__}: {error})")
        print(f"\n{total_cogs} cog(s) found. {imported_cogs} cog(s) successfully loaded.")
        
        if imported_cogs == 0:
            print("Nothing loaded, terminating bot.")
            sys.exit()
        
        guild = discord.Object(1005139715588112454)
        self.tree.copy_global_to(guild = guild)
        synced = await self.tree.sync(guild = guild)
        print(f"{len(synced)} commands synced at guild {guild.id}.")

    async def on_ready(self):
        print(f'{bot.user.name} connected.')
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST,PORT))
            s.listen()
            print(f"Server Listening on {HOST}:{PORT}")
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
    
bot = troubleshooter()
bot.run(bot.secret_sauce("BOT_TOKEN"))
