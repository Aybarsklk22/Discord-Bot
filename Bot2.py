import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='1', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def topla(ctx,s1=0,s2=0):
    await ctx.send(s1+s2)

@bot.command()
async def çıkar(ctx,s1=0,s2=0):
    await ctx.send(s1-s2)

@bot.command()
async def zar(ctx, tahmin=0):
    sonuç = random.randint(1,6)
    if tahmin == sonuç:
        await ctx.send('Doğru bildin!!!!')
    else:
        await ctx.send(f'Bu sefer tutmadı birdahakine.Doğru cevap {sonuç}')











bot.run("MTI4MzQ2NTkwNjY1OTUyODc1NQ.GmDLx1.Qng8XD_C1dzvPisi8txepWypstmjsNkIKWZ0")
