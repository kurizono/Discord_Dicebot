from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


#@bot.command()
#async def ping(ctx):
#    await ctx.send('pong')

#async def on_message(message):
    #if message.content == '/neko':
    #    await message.channel.send('にゃーん')
    # elif message.content == '/dice':
    #    await message.channel.send('diceだよ')
    # 開始ワード
    #elif message.content.startswith('dice'):
    #    # メッセージ送信者がBotだった場合は無視する
    #    if message.author.bot:
    #        return
    #    # 「/neko」と発言したら「にゃーん」が返る処理
    #    await message.channel.send('ダイスbot起動')

@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')



token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
