import json
import time
from datetime import datetime
import discord
import asyncio
import os
from mega import Mega


async def dm(msg, message, client):
    id = str(msg.author.id)
    author = str(msg.author)
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    if id == "559789590064529408":
        m = message.split(";")
        if m[0] == "send":
            user = client.get_user(int(m[1]))
            await user.send("".join(m[2]))
    else:
        with open("feedback.json") as f:
            fb = json.load(f)
        try:
            if fb[id]["blocked"]:
                await msg.channel.send("Really sorry but you have been blocked, this is most likely due to spam. I will not be able to receive your feedback.")
                return
            try:
                fb[id][date].append(message)
            except KeyError:
                fb[id][date] = [message]
        except:
            fb[id] = {
                "blocked": False,
                "user": author,
                date: [message]
            }
        with open("feedback.json", "w") as f:
            json.dump(fb, f, indent=2)
        await msg.channel.send("Your feedback has been saved.")


async def feedback(msg, message):
    await msg.reply("Great, please message me your feedback.")
    await msg.author.send("You can give me your feedback here.")


async def define(msg, message):
    word = " ".join(message.split(" ")[1::])
    word = word.capitalize()
    with open("dictionary.txt") as f:
        definition = f.read().split(word)[1].split("\n")[0]
        await msg.reply(definition)


async def set_timer(msg, message):
    t = float(message.split(" ")[1])
    await msg.reply(f"Timer set for {t} minute(s)")
    await asyncio.sleep(t*60)
    await msg.reply("Time's Up")


async def wordsearch(msg, message):
    await msg.reply("To play wordsearch create a channel and call it \"wordsearch\"", file=discord.File('wordsearch/channel.png'))


async def create_grid(msg, message):
    await msg.channel.send(file=discord.File('grid.png'))

async def download(msg, message):
    url = message.split(" ")[1]
    await msg.reply(f"[youtube] {url.split('watch?v=')[1]}: Downloading video")
    try:
        output = os.popen(f"cd ./videos; yt-dlp \"{url}\"; cd ..").read()
    except Exception as e:
        await msg.reply(e)
    video = output.split('[Merger]')[1].split('"')[1]
    await msg.reply(f"[download] 100%\n[download] {video}: Uploading video")
    mega = Mega()
    m = mega.login()
    try:
        destination = os.path.join("./videos", video)
        file = m.upload(destination)
    except Exception as e:
        await msg.reply(e)
    print(m.get_upload_link(file))
    await msg.reply(f"[mega] {m.get_upload_link(file)}: Uploaded video")


run = {
    "dm": dm,
    "feedback": feedback,
    "define": define,
    "timer": set_timer,
    "wordsearch": wordsearch,
    "download": download
}