from discord.ext import commands
import ctypes
import discord
import os
import requests
import time
import json
from colorama import Fore, init, Style
import subprocess
import ctypes
import random
import string
import threading
import asyncio
import hashlib
import socket
import discord
from discord.ext import commands
import os
from lxml import html
import urllib.request
import sys
import requests
from threading import Thread
import time
import platform
from queue import Queue

ctypes.windll.kernel32.SetConsoleTitleW("twitch bot")


token = ''
prefix = '?'
bot = commands.Bot(command_prefix=prefix, case_insensitive=True)
bot.remove_command('help')
authorized_channels = [698609799482572890, 699471430357745757]


@bot.event
async def on_ready():
    print(Style.BRIGHT + Fore.WHITE + '{}#{} | {}\n'.format(str(bot.user.name), str(bot.user.discriminator), str(bot.user.id)))
    print("Bot made by cupiditys#0001")
    print("-----------------------------------------------------------")
    activity = discord.Activity(type=discord.ActivityType.playing, name="dyno.gg | ?help")
    await bot.change_presence(activity=activity)


@bot.command(pass_context=True)
@bot.event
async def follow(ctx, channel, amount: int):
    role = discord.utils.get(ctx.message.guild.roles, name="Developers")
    if role in ctx.message.author.roles:
        max_amount = 112636
    else:
        max_amount = 5500
    if amount > max_amount:
        embed = discord.Embed(title="**Error**", color=000000, description=f"The amount {amount} is higher then the max amount: {max_amount}!")
        await ctx.channel.send(embed=embed)
    if amount <= max_amount:
        embed = discord.Embed(title="**Follow**", color=0x6441a5, description=f"Sending {amount} followers to {channel}!")
        embed.set_footer(text='{}#{}'.format(ctx.message.author.name, ctx.message.author.discriminator), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/686048368489005074/688128260345036811/twitch.png')
        await ctx.channel.send(embed=embed)
        def start_follow(to_follow):
                try:
                    sent_followers = 0
                    counter2 = 0
                    usernames = []
                    global following
                    following = True
                    get_uid = requests.get('https://api.twitch.tv/helix/users?login=' + to_follow, headers={'Client-Id':'kimne78kx3ncx6brgo4mv6wki5h1ko'})
                    uid = str(get_uid.json()['data'][0]['id'])
                    with open('oauth.txt', 'r') as f:
                        lines = [line.strip() for line in f]
                        for x in lines:
                            try:
                                usernames.append(x.split(':')[-1])
                            except Exception as e:
                                # print(e)
                                pass

                    def follow_user(oauth, uid):
                        try:
                            c = requests.Session()
                            oauth = 'OAuth ' + oauth
                            headers = {
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
                                'Origin': 'https://www.twitch.tv',
                                'Referer': 'https://www.twitch.tv/' + str(to_follow),
                                'Content-Type': 'text/plain;charset=UTF-8',
                                'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                                'Authorization': oauth,
                                'Accept-Language': 'en-US'
                                }
                            data = '[{\"operationName\":\"FollowButton_FollowEvent_User\",\"variables\":{\"id\":\"'+uid+'\"},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"026fcca256d4ef52efaf92e922ff1d16e9cb2f9de8d3731c1074f5a0118d7670\"}}},{\"operationName\":\"FollowButton_FollowUser\",\"variables\":{\"input\":{\"disableNotifications\":false,\"targetID\":\"'+uid+'\"}},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"51956f0c469f54e60211ea4e6a34b597d45c1c37b9664d4b62096a1ac03be9e6\"}}}]'
                            send_follow = c.post('https://gql.twitch.tv/gql', headers=headers, data=data)
                            # ctypes.windll.kernel32.SetConsoleTitleW("Sent a total of " + str(sent_followers) + ' followers!')
                        except:
                            pass
                        
                    while following is True:
                        if threading.active_count() <= 250:
                            try:
                                threading.Thread(target=follow_user, args=(usernames[counter2],uid,)).start()
                                counter2 += 1
                                sent_followers += 1
                                # time.sleep(0.03)
                            except Exception as e:
                                # print(e)
                                pass
                        if sent_followers >= len(usernames):
                            following = None
                            sent_followers = 0
                except Exception as e:
                    # print(e)
                    pass
        start_follow(channel)


@bot.command(pass_context=True)
@bot.event
async def unfollow(ctx, channel, amount: int):
    role = discord.utils.get(ctx.message.guild.roles, name="Developer")
    if role in ctx.message.author.roles:
        max_amount = 112636
    else:
        max_amount = 7000
    if amount > max_amount:
        await ctx.send(f'[{ctx.author.mention}] Error! The amount {amount} is higher than the max amount: {max_amount}')
    if amount <= max_amount:
        embed = discord.Embed(title="**Unfollow**", color=000000, description=f"Removing {amount} followers from {channel}!")
        embed.set_footer(text='{}#{}'.format(ctx.message.author.name, ctx.message.author.discriminator), icon_url=ctx.message.author.avatar_url)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/686048368489005074/688128260345036811/twitch.png')
        await ctx.channel.send(embed=embed)

        def start_follow2(to_follow):
            try:
                sent_followers = 0
                counter2 = 0
                usernames = []
                global following
                following = True
                get_uid = requests.get('https://api.twitch.tv/helix/users?login=' +
                                       to_follow, headers={'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko'})
                uid = str(get_uid.json()['data'][0]['id'])
                with open('oauth.txt', 'r') as f:
                    lines = [line.strip() for line in f]
                    for x in lines:
                        try:
                            usernames.append(x.split(':')[-1])
                        except:
                            pass

                def follow_user(oauth, uid):
                    try:
                        c = requests.Session()
                        oauth = 'OAuth ' + oauth
                        headers = {
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
                            'Origin': 'https://www.twitch.tv',
                            'Referer': 'https://www.twitch.tv/' + str(to_follow),
                            'Content-Type': 'text/plain;charset=UTF-8',
                            'Client-Id': 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                            'Authorization': oauth,
                            'Accept-Language': 'en-US'
                        }
                        data = '[{\"operationName\":\"FollowButton_UnfollowUser\",\"variables\":{\"input\":{\"targetID\":\"'+uid + \
                            '\"}},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"d7fbdb4e9780dcdc0cc1618ec783309471cd05a59584fc3c56ea1c52bb632d41\"}}}]'
                        c.post('https://gql.twitch.tv/gql',
                               headers=headers, data=data)
                    except:
                        pass

                while following is True:
                    if threading.active_count() <= 500:
                        try:
                            threading.Thread(target=follow_user, args=(
                                usernames[counter2], uid,)).start()
                            counter2 += 1
                            sent_followers += 1
                        except:
                            pass
                    if sent_followers >= len(usernames) or sent_followers > amount:
                        following = None
                        sent_followers = 0
            except:
                pass

        start_follow2(channel)

    else:
        pass
bot.run(token)