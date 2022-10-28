import discord


def connect(token):
    _client = discord.Client(intents=discord.Intents.all())
    @_client.event
    async def on_ready():
        print("Logged in as {0.user}".format(_client))
    _client.run(token)

    return _client