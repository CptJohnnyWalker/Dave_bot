import discord
import asyncio
import random
import json
import cleverbot

cb1 = cleverbot.Cleverbot()
cb2 = cleverbot.Cleverbot()
cb3 = cleverbot.Cleverbot()
cb4 = cleverbot.Cleverbot()
cb5 = cleverbot.Cleverbot()

client = discord.Client()
messages_db = []

async def conversation_interface(message):
    cb = cb5
    user = str(message.author)
    if user == "Maurice":
        cb = cb1
        print(user)
    if user == "Captain Johnny Walker":
        cb = cb2
        print(user)
    if user == "Baughb42":
        cb = cb3
        print(user)
    if user == "Bigbidoof":
        cb = cb4
        print(user)

    question = str(message.content)[22:]
    print(question)
    msg = cb.ask(question)
    await client.send_message(message.channel, msg)

async def command_interface(message):
    command = str(message.content).split()

    if command[1] == "quit":
        with open("database", 'w') as output:
            json.dump(messages_db, output)

        client.close()
        client.logout()

    if command[1] == "quote":
        message_list = []
        for user in messages_db:
            if user[1] == command[2]:
                message_list.append(user)
        for user in message_list:
            if user[0] == command[3]+ ' ' + command[4]:
                msg = "%s said, \"%s\" on %s" % (user[1], user[2], user[0])
                await client.send_message(message.channel, msg)

    if command[1] == "dice":
        sidesn = int(command[2])
        msg = random.randrange(1,sidesn,1)
        await client.send_message(message.channel, msg)

    if command[1] == "help":
        await client.send_message(message.channel, "quote name yyyy-mm-dd 24hr:time")
        await client.send_message(message.channel, "dice sides")



@client.event
async def on_ready():
    print(client.user.name)
    with open("database", 'w') as input_f:
        messages_db = json.dumps(input_f)

@client.event
async def on_message(message):

    message_info = [str(message.timestamp)[0:16], str(message.author), str(message.content)]
    messages_db.append(message_info)

    print(message_info)

    if message.content.startswith('!command'):
        await command_interface(message)
    if message.content.startswith('<@157179616816136201>'):
        await conversation_interface(message)



client.run("", "")
