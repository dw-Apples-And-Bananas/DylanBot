import random
import time
import string
import discord
import wordsearch.grid as image_grid


class Game():
    def __init__(self, msg):
        self.size = 12
        self.rules = ["l", "r", "u", "d"]
        self.msg = msg
        with open("words.txt") as f:
            self.words_file = f.read().split("__")
    

    async def start(self):
        grid = []
        for i in range(self.size):
            grid.append("".join(["." for n in range(self.size+1)]))
        words = []
        for i in range(5):
            while True:
                word = random.choice(self.words_file).lower()
                if len(word) <= 5 and len(word) >= 3:
                    break
            words.append(f"{word}\n")

        for word in words:
            x = random.randint(0, self.size)
            y = random.randint(0, self.size)
            positions = self.direct(word, [y,x], random.choice(self.rules))
            try:
                for i, pos in enumerate(positions):
                    g = list(grid[pos[0]])
                    if g[pos[1]] == ".":
                        g[pos[1]] = word[i]
                    else:
                        await self.msg.channel.send("collision")
                    grid[pos[0]] = "".join(g)
            except Exception as e:
                await self.msg.channel.send(e)

        image_grid.png(self.format_grid(grid), self.size)
        await self.msg.channel.send(file=discord.File('grid.png'))
        # await self.msg.channel.send("".join(self.format_grid(grid)))
        # print("".join(self.format_grid(grid)))
    

    def direct(self, word, pos, d):
        xrule = 0
        yrule = 0
        if d == "r":
            xrule, yrule = 1, 0
            if pos[1] > self.size-len(word):
                pos[1] -= pos[1]-(self.size-len(word))
        elif d == "u":
            xrule, yrule = 0, -1
        elif d == "d":
            xrule, yrule = 0, 1
        elif d == "l":
            xrule, yrule = -1, 0
            if pos[1] < len(word):
                pos[1] += len(word)-pos[1]

        x = [pos[1]]
        y = [pos[0]]
        for i in range(len(word)-2):
            x.append(x[-1]+xrule)
        for i in range(len(word)-2):
            y.append(y[-1]+yrule)
        return [[y[i],x[i]] for i in range(len(x))]

    
    def format_grid(self, grid):
        _grid = []
        for y in grid:
            line = ""
            for x in y:
                if x == ".":
                    x = random.choice(string.ascii_letters).upper()
                line += x.upper()
            _grid.append(line)
        return _grid
