from discord.ext import commands
from os import getenv
import traceback

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
        await bot.send_message(message.channel, 'Done sleeping')

@bot.commands()
async def ping(ctx):
    await ctx.send('pong')

@bot.commands()
async def dice10(ctx):
    await ctx.send('1~10')

@bot.commands()
async def dice100(ctx):
    await ctx.send('1~100')


token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
