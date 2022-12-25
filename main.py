from copy import deepcopy
import random
import discord
from discord import app_commands
from discord.ext import commands
import draw as d
import gen as g
import map as m
import bottoken

nl = '\n'

intents = discord.Intents.default()
intents.message_content = True
#intents.members = True
client = commands.Bot(command_prefix='&',intents=intents,help_command=None)
client.games = {}
client.drawsettings = {
    "size": 20
}
client.settings = {
    "expansiveness": 3
}

testmap = """111111110011
111110110111
111110111110
111000111110
111111111110
111111111010
111111111010
111101110010
111100110011
111100000011
011111000111
001111000111"""

class Game:
    def __init__(self,map,nations,col,year = 0):
        self.map = map
        self.nations = nations
        self.col = col
        self.key = dict(zip(self.nations,self.col))
        self.year = year
    def refresh(self):
        self.key = dict(zip(self.nations, self.col))
    def freecol(self):
        while True:
            c = random.choice(list(self.key.keys()))
            if c not in self.nations:
                return self.key[c]

@client.event
async def on_ready():
    p = await client.tree.sync(guild=discord.Object(1056005072775032912))
    print(f"Synced {p}")
    print("ok, ready")

@app_commands.command()
@app_commands.guilds(discord.Object(1056005072775032912))
async def run(ctx: discord.Interaction):
    """Runs the game, or starts it if there aren't any in this channel"""

    #setup
    if ctx.channel_id not in list(client.games.keys()):
        col = list(d.c.names.keys())
        random.shuffle(col)
        game = client.games[ctx.channel_id] = Game(
            map = deepcopy(testmap),
            nations = [g.word().title() for _ in range(5)],
            col = col
        )
        for i in game.nations:
            spot = m.randomunclaimed(game.map)
            game.map = game.map[:spot] + d.c.names[game.key[i]] + game.map[spot+1:]
    else:
        game = client.games[ctx.channel_id]

    def color(n):
        return d.c.names[game.key[n]]
    def setpos(pos,c):
        return game.map[:pos] + c + game.map[pos + 1:]
    def expand(n,strength=1,o=False):
        if o:
            t = random.choice(m.getfriendlyneighbors(game.map,color(n),o))
        else:
            t = random.choice(m.allofcolor(game.map, color(n)))
        game.map = setpos(m.rlandneighbor(game.map, t), color(n))
        if strength > 1 and m.getfriendlyneighbors(game.map,color(n),t):
            expand(n,strength=strength-1,o=t)

    #auto stuff
    game.year += 1
    if game.year > 1:
        for i in game.nations:
            if not m.allofcolor(game.map, color(i)):
                del game.nations[game.nations.index(i)]
                continue
            exp = client.settings["expansiveness"]
            for _ in range(random.randint(0,round(exp*1.5))):
                expand(i,strength=2)
        if random.random() < 0.1 and len(game.nations) < 5:
            n = g.word().title()
            game.nations.append(n)
            game.col.append(game.freecol())
            game.refresh()

    #draw
    img = d.drawr(d.convert(game.map),settings=client.drawsettings)
    if isinstance(img, str):
        await ctx.response.send_message(f"An error occurred: {img}")
    else:
        img.save("temp.png")
        await ctx.response.send_message(f"Year {game.year}\nNations:\n{nl.join([f'{i} ({j})' for i, j in zip(game.nations,game.col)])}", file=discord.File("temp.png"))

client.tree.add_command(run)

client.run(bottoken.token)