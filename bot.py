import discord
from discord.ext import commands
import asyncio
 
bot=commands.Bot(command_prefix='D')
 
@bot.event
async def on_ready():
    print('The bot is ready!')
    print(bot.user.name)
    print(bot.user.id)
   
   
bot.run('NTQxOTExODM3OTYxMDkzMTIw.D2LW6w.tAT1-IK2Ut-RywgF9CCIjeOr3Jo')
