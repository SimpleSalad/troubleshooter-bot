import os
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents,
                   command_prefix='fn$',
                   owner_id = 88087496189022208,
                   status = discord.Status.do_not_disturb,
                   activity = discord.Game(name = "Dungeon Fighter Online", type = discord.ActivityType.competing))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(f'{bot.user.name} connected.')
    

bot.run(TOKEN)