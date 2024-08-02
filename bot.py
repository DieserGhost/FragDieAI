import discord
from discord.ext import commands
from g4f.client import Client
import nest_asyncio

nest_asyncio.apply()

client = Client()

intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
  print(f'Angemeldet als {bot.user}')

@bot.command()
async def ask(ctx, *, question):
  try:
    response = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": f"Antwort auf Deutsch: {question}"}],
    )
    await ctx.send(response.choices[0].message.content.strip())
  except Exception as e:
    await ctx.send(f"Ein Fehler ist aufgetreten: {e}")

bot.run('DEIN DISCORD TOKEN ')
