from discord.ext import commands
from os import getenv
import traceback
from ast import parse

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.event
async def on_message(message):
    if message.author != bot.user:
        await message.channel.send(message.content)
    



token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
