import interactions
from dadjokes import Dadjoke
import randfacts
import requests

token = open("token.txt", "r")

guild = id

bot = interactions.Client(token=token.readline())

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
          "name": "/duck",
          "value": "Use this command to see an image of a cute duck"
        }],
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
    name="duck",
    description="I will show you an image of a duck",
    scope=guild,
)

async def help(ctx: interactions.CommandContext):
    duck = "https://random-d.uk/api/randomimg"
    embed = interactions.Embed(
    image={
        "url": duck,
        "height": 0,
        "width": 0
      },
    footer={
        "text": "Powered by random-d.uk"
      },
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
          "name": "Duck Images",
          "value": "  https://random-d.uk/\n"
        },
        {
          "name": "Dad Jokes",
          "value": "https://pypi.org/project/dadjokes/"
        },
        {
          "name": "Random Facts",
          "value": "https://pypi.org/project/randfacts/"
        }
      ],
    color=interactions.Color().yellow,)
    await ctx.send(embeds=embed)








bot.start()