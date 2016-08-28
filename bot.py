import discord
import asyncio
import random
import json
import cleverbot
import json
from urllib.request import urlopen

#########################################################
#Globals

cb = cleverbot.Cleverbot()
client = discord.Client()
hypedb = ["http://i.imgur.com/1oNSmyl.gif",
          "http://gifs.benlk.com/happening.gif",
          "https://31.media.tumblr.com/4631d343dd011414e886977c73a6bb03/tumblr_n58fqtFyTj1svlwhbo1_1280.gif",
          "http://s3.amazonaws.com/rapgenius/funny-gif-Colbert-screaming.gif",
          "https://fat.gfycat.com/ActualFeistyBettong.gif",
          "http://1.bp.blogspot.com/-V0lGJz82ijw/UsnKIAqEp1I/AAAAAAAAA6E/mdmU5rJwBGw/s1600/RIVAHHSSSHYPED.gif",
          "https://49.media.tumblr.com/4581c0f0a529da432bf5ac84e3d5de0a/tumblr_ncj65sNEnd1sr6y44o1_500.gif"
          ]

#########################################################
#Helper fucntions

async def AppendId(message, msg):
    msg += "<@%s> " % (message.author.id)
    return msg
#########################################################
#Events

@client.event
async def on_ready():
    print(client.user.name)

    
@client.event
async def on_message(message):
    if client.user.id in message.content:
        await MessageParse(message)

async def MessageParse(message):
    message_array = str(message.content).split()

    if message_array[1] == "!hype":
        await Hype(message)
    else:
        await Cleverbot(message)

##########################################################
#Actions
async def Cleverbot(message):
    question = str(message.content)[22:]
    msg = ''
    msg = await AppendId(message, msg)
    msg += cb.ask(question)
    await client.send_message(message.channel, msg)

async def Hype(message):
    msg = ''
    msg = await AppendId(message, msg)
    msg += random.choice(hypedb)
    await client.send_message(message.channel, msg)
    
##########################################################
#Connection
               
client.run("pinkfloyd6000@gmail.com", "bono01")
