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
    # 開始ワード
    if message.content.startswith('dice'):
        # メッセージが送られてきたチャンネルへメッセージを送ります
        await bot.send_message(message.channel, "aaaa")
    



token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
