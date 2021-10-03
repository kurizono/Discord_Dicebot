from discord.ext import commands
from os import getenv
import traceback

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def on_message(message):
    if message.author.bot:
        return

    if message.contentt.startswith("dice"):
        await message.channel.send("dice")
    elif message.content == '/test':
        await message.channel.send("aaaa")
    



token = getenv('DISCORD_BOT_TOKEN')
bot.run(token)
