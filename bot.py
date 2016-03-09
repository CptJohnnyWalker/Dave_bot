import discord
import asyncio
import json

client = discord.Client()
messages_db = []

async def conversation_interface(message):
    await client.send_message(message.channel, "Yes.")

async def command_interface(message):
    command = str(message.content).split()
    if command[1] == "quote":
        message_list = []
        for user in messages_db:
            if user[1] == command[2]:
                message_list.append(user)
        for user in message_list:
            if user[0] == command[3]+ ' ' + command[4]:
                msg = "%s said, \"%s\" on %s" % (user[1], user[2], user[0])
                await client.send_message(message.channel, msg)


@client.event
async def on_ready():
    print(client.user.name)

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
