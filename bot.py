import os
import random
import discord
from discord.ext import tasks

TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = 1553284797143715850

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

memes = [
    "https://i.imgflip.com/30b1gx.jpg",
    "https://i.imgflip.com/1bij.jpg",
    "https://i.imgflip.com/1ur9b0.jpg"
]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

    if not post_meme.is_running():
        post_meme.start()

@tasks.loop(minutes=5)
async def post_meme():
    channel = bot.get_channel(CHANNEL_ID)

    if channel is None:
        print("Channel not found!")
        return

    meme_url = random.choice(memes)

    embed = discord.Embed()
    embed.set_image(url=meme_url)

    await channel.send(embed=embed)
    print("Meme sent successfully!")

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is not set!")

bot.run(TOKEN)
