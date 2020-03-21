#title           :Insult Bot.py
#description     :A bot that insults.
#author          :Harsimran Grewal (Retr0-Flow on github)
#date            :23/8/2019
#version         :3.0
#usage           :Put in your discord token and have fun.
#notes           : Any friendship destroyed is not my fault.
#python_version  :3.7.0
#==============================================================================


import discord
import os
import random

token = 'YOUR TOKEN HERE'
TOKEN = token

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!a'):			#allows users to do a everyone callout
        msg = '@everyone ' + message.content[2:]
        await client.send_message(message.channel, msg)

    if message.content.startswith('!t'):			#basic debug command
        msg = str(message.content) + ' | ' + str(message.channel)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!insult'):			#will whoever you specify after the invoke
        fileOpen = open(r'./insults.txt', 'r')
        rand = random.randint(0,10004)
        perIns = message.content[7:]
        for line in fileOpen:
            x = line.split('|')
            print(x[rand])
        await client.send_message(message.channel, (x[rand] %perIns))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
