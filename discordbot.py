from discord.ext import commands
from os import getenv
import traceback
from ast import parse
import asyncio

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.event
async def on_message(message):
    if message.content.startswith('dice'):
        await bot.send_message(message.channel, 'this is dicebot')

    if message.content.startswith('!test'):
        counter = 0
        tmp = await bot.send_message(message.channel, 'Calculating messages...')
        async for log in bot.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await bot.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await bot.send_message(message.channel, 'Done sleeping')
    

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
