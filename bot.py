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
rossb = ["http://3.bp.blogspot.com/-XxbTk4t1bpA/UI_PJi1BABI/AAAAAAAABgg/tnOiIsB2dKY/s1600/bob_ross_csg024_autumn_glory.jpg", 
         "http://artforsaleamerica.com/paintings-image/bob-ross/bob-ross-sun-after-rain-86142.jpg",
         "http://1.bp.blogspot.com/-YujIJyDFHLE/UI_Ovw_VuFI/AAAAAAAABfw/XWMIIKg_9PI/s1600/bob_ross_csg015_twilight_meadow.jpg",
         "http://2.bp.blogspot.com/_pT-Sqkrybuk/TG5Xo7l2hBI/AAAAAAAAAGY/bLY1zmnl7oQ/s1600/bob-ross-landscape-painting-281-2.jpg",
         "http://www.deshow.net/d/file/cartoon/2008-12/bob-ross-oil-painting-282-46.jpg",
         "http://img.xcitefun.net/users/2009/03/41037,xcitefun-bob-ross-paintings-beautiful-4.jpg",
         "http://4.bp.blogspot.com/-pkpOG2oWDi0/UJL0PbUpEnI/AAAAAAAAGz0/aAslDaF1M2o/s1600/bob+ross+1.jpg",
         "http://1.bp.blogspot.com/-0tPGQRWyrV8/UJL0dsrq-6I/AAAAAAAAG08/TdSulvFVmik/s1600/bob+ross+18.jpg",
         "http://3.bp.blogspot.com/-a_UGVnmjghk/UajazIi6eyI/AAAAAAAAC6U/VDAuzdUg81Y/s1600/bob-ross-landscape-oil-painting-27-18.jpg",
         "http://www.saleoilpaintings.com/paintings-image/bob-ross/bob-ross-natures-grandeur-86102.jpg",
         "http://www.saleoilpaintings.com/paintings-image/bob-ross/bob-ross-purple-haze-86115.jpg",
         "http://www.saleoilpaintings.com/paintings-image/bob-ross/bob-ross-mountain-sunset-86095.jpg"
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
    elif message_array[1] == "!ross":
              await Ross(message)
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
    
async def Ross(message):
    msg = ''
    msg = await AppendId(message, msg)
    msg += random.choice(rossb)
    await client.send_message(message.channel, msg)
##########################################################
#Connection
               
client.run("pinkfloyd6000@gmail.com", "bono01")
