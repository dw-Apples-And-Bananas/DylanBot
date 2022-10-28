import discord
from info import *
import log
import cmds
import wordsearch.cmds


client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.event
async def on_message(msg):
    if msg.author == client.user:
        return
    message = str(msg.content).lower()

    if isinstance(msg.channel, discord.DMChannel):
        await cmds.run["dm"](msg, message, client)

    if message.startswith("dylan, "):
        log.message(msg)
        message = message.replace("dylan, ", "")
        try:
            await cmds.run[message](msg, message)
        except:
            try:
                await cmds.run[message.split(" ")[0]](msg, message)
            except:
                pass
    else:
        if msg.channel.name == "wordsearch":
            try:
                await wordsearch.cmds.run[message](msg, message)
            except:
                pass


client.run(TOKEN)