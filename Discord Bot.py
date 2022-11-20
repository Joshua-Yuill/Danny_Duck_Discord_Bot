import discord
from dadjokes import Dadjoke
import randfacts

f = open("token.txt", "r")

 
intents = discord.Intents.all()
client = discord.Client(command_prefix='/', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
count = 0

@client.event
async def on_message(message):
    print("message-->", message)
    if message.author == client.user:
        return
    
    if message.content.startswith('hi'):
        await message.channel.send("Hello!")
 
    if message.content.startswith('dad' or 'Dad'):
        dadjoke = Dadjoke()
        await message.channel.send(dadjoke.joke)
        
    if message.content.startswith('quack' or 'Quack'):
        await message.channel.send("**Quack Quack!**")
        
    if message.content.startswith('fact' or 'Fact'):
        fact = randfacts.get_fact()
        await message.channel.send(fact) 
        
        
 
client.run(f.readline())