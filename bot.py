import discord
import asyncio
import random
import json

client = discord.Client()
messages_db = []

async def conversation_interface(message):
    await client.send_message(message.channel, "Yes.")

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
        dicen = int(command[3])
        msg = ''
        while dicen > 0:
            randn = sidesn % random.random()
            msg += "%d " % (randn)
            dicen -= 1
        await client.send_message(message.channel, msg)

    if command[1] == "help":
        await client.send_message(message.channel, "quote name yyyy-mm-dd 24hr:time")
        await client.send_message(message.channel, "dice sides numDice")



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
    if message.content.startswith('Dave'):
        await conversation_interface(message)



client.run("", "")
