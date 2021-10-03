from discord.ext import commands
from os import getenv
import traceback
import random

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def dice(ctx):
    await ctx.send('1~100')

@bot.event
async def on_message(message):
    #ちゃんとしたユーザーがメッセージ
    if message.author == bot.user:
        return
    #diceから始まる
    if message.content.startswith('dice'):
        m = random.randint(1,100)
        await message.channel.send(m)

token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
