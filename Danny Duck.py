import interactions
from dadjokes import Dadjoke
import randfacts
import math
import random
import time

#Bot Authentication Details
token = open("token.txt", "r")

guild = id

bot = interactions.Client(token=token.readline())
#===============================================================

#Global Variables
health = 255
clean = 255
happy = 255
hunger = 255

timeFood = time.time()
timeClean = time.time()
timeHappy = time.time()
timeHealth = time.time()

@bot.command(
    name="help",
    description="Hi I am Danny Duck, lets get to know each other better!",
    scope=guild,
)

async def help(ctx: interactions.CommandContext):
    embed = interactions.Embed(
    title="Hi! I am Danny Duck! You're Helpful Ducky Assistant",
    description="",
    fields=[
        {
          "name": "/help",
          "value": "Displays this message (Nice!)"
        },
        {
          "name": "/quack",
          "value": "I am quackers for you, and I will say it."
        },
        {
          "name": "/joke",
          "value": "Use this command to make me tell a Joke"
        },
        {
          "name": "/fact",
          "value": "Use this command to make me say an intresting fact"
        },
        {
          "name": "/clean",
          "value": "Use this command to clean me"
        },
        {
          "name": "/feed",
          "value": "Use this command to feed me some food"
        },
        {
          "name": "/activity",
          "value": "Use this command to play a game with me!"
        },
        {
          "name": "/stats",
          "value": "Use this command to see my statistics, like hunger, happiness and cleanliness"
        },
        {
          "name": "/history",
          "value": "Use this command to see who most recently fed, cleaned and played with me"
        },
        {
          "name": "/attribution",
          "value": "Use this command to see who made this bot possible"
        },
        ],
    thumbnail={
        "url": "https://cdn.discordapp.com/attachments/804177032137146429/1044011439049941093/IMG_0929.jpg",
        "height": 0,
        "width": 0,
      },
    color=interactions.Color().yellow,)
    await ctx.send(embeds=embed)


@bot.command(
    name="quack",
    description="Quack",
    scope=guild,
)

async def quack(ctx: interactions.CommandContext):
    embed = interactions.Embed(
    title="Quack Quack!",
    color=interactions.Color().yellow,)
    await ctx.send(embeds=embed)


@bot.command(
    name="fact",
    description="I will tell you an intresting fact you might not know.",
    scope=guild,
)

async def fact(ctx: interactions.CommandContext):
    fact = randfacts.get_fact()
    embed = interactions.Embed(
    title=fact,
        author={
        "name": "Fact:"},
    footer={
        "text": "Powered by Randfacts"
    },
    color=interactions.Color().yellow,)
    await ctx.send(embeds=embed)

@bot.command(
    name="joke",
    description="I will tell you a top quality dad joke.",
    scope=guild,
)

async def joke(ctx: interactions.CommandContext):
    dadjoke = Dadjoke()
    embed = interactions.Embed(
    title=dadjoke.joke,
    author={
        "name": "Joke:"},
    footer={
        "text": "Powered by dadjokes 1.3.2 API"
    },
    color=interactions.Color().yellow,)
    await ctx.send(embeds=embed)




@bot.command(
    name="stats",
    description="See my stats",
    scope=guild,
)

async def help(ctx: interactions.CommandContext):
  
    foodEffect = (time.time() - timeFood)
    cleanEffect = (time.time() - timeClean)
    happyEffect = (time.time() - timeHappy)
    healthEffect = (time.time() - timeHealth)
    thumb = ""
    
    if int(((health-healthEffect)/255)*100) < 1:
      healthColour = interactions.Color().black
      thumb = "https://cdn.discordapp.com/attachments/815712795344764938/1045455508041117807/istockphoto-1148649898-612x612.jpg"
    
    elif int(((health-healthEffect)/255)*100) < 15:
      healthColour = interactions.Color().red
      thumb = "https://cdn.discordapp.com/attachments/804177032137146429/1044011439049941093/IMG_0929.jpg"
      
    elif int(((health-healthEffect)/255)*100) < 70:
      healthColour = interactions.Color().yellow
      thumb = "https://cdn.discordapp.com/attachments/804177032137146429/1044011439049941093/IMG_0929.jpg"
    
    else:    
      healthColour = interactions.Color().green
      thumb = "https://cdn.discordapp.com/attachments/804177032137146429/1044011439049941093/IMG_0929.jpg"

    
    embed = interactions.Embed(
    fields=[
      {
        "name": "**Health**",
        "value": str(math.trunc(((health-healthEffect)/255)*100))+"%",
        "inline": True
      },
      {
        "name": "**Happiness**",
        "value": str(math.trunc(((happy-happyEffect)/255)*100))+"%",
        "inline": True
      },
      {
        "name": "**Cleanliness**",
        "value": str(math.trunc(((clean-cleanEffect)/255)*100))+"%",
        "inline": True
      },
      {
        "name": "**Hunger**",
        "value": str(math.trunc(((hunger-foodEffect)/255)*100))+"%",
        "inline": True
      },
      ],
    author={
        "name": "Stats:"},
    footer={
        "text": ""
    },
    thumbnail={
        "url": thumb,
        "height": 0,
        "width": 0,
      },
    color=healthColour,)
    await ctx.send(embeds=embed)
    
    
@bot.command(
    name="feed",
    description="Feed me!",
    scope=guild,
)

async def feed(ctx: interactions.CommandContext):
    global timeFood
    timeFood = time.time()
    embed = interactions.Embed(
    title="Yum Yum!",
    color=interactions.Color().yellow,)
    await ctx.send(embeds=embed)
    
@bot.command(
    name="clean",
    description="Clean me!",
    scope=guild,
)

async def feed(ctx: interactions.CommandContext):
    global timeClean
    timeClean = time.time()
    embed = interactions.Embed(
    title="Scrub-a-dub!",
    color=interactions.Color().yellow,)
    await ctx.send(embeds=embed)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

@bot.command(
    name="attribution",
    description="Thanks to individuals and services that supported this project",
    scope=guild,
)

async def help(ctx: interactions.CommandContext):
    duck = "https://random-d.uk/api/randomimg"
    embed = interactions.Embed(
    title="Attribution",
    description="With thanks to:",
    fields=[
        {
          "name": "Terrorfusion",
          "value": "For conceptulisation and support"
        },
        {
          "name": "Duck Images",
          "value": "https://random-d.uk/\n"
        },
        {
          "name": "Dad Jokes",
          "value": "https://pypi.org/project/dadjokes/"
        },
        {
          "name": "Random Facts",
          "value": "https://pypi.org/project/randfacts/"
        },
      ],
    color=interactions.Color().yellow,)
    await ctx.send(embeds=embed)








bot.start()