from wordsearch.game import Game


async def play(msg, message):
    await Game(msg).start()


async def help(msg, message):
    await msg.channel.send("**How To Play Dylan's WordSearch Game:**\n\t•test")


run = {
    "play": play,
    "help": help,
    "how to play": help
}