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
        info = parse('dice {}d{} {}', message.content)
        if info:
            if info[1].isdecimal() and info[0].isdecimal():
                dice_num = int(info[0])
                dice_size = int(info[1])
                key = info[2]
                # メッセージを書きます
                m = message.author.name + ' '
                await bot.send_message(message.channel, m)
    



token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
