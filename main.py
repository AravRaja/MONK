import discord
import os
import asyncio
from keepAlive import keep_alive  #connects to http server
from replit import db
import game  #holds game classes which r used to initiate games
from message import success
from leaderboard import leaderboard
import embed
from discord.ext import commands
from discord.ext import tasks
from math import ceil as c
import time

intents = discord.Intents.default()
client = commands.Bot(command_prefix='-', description='A game discord bot', intents=intents)
@client.event
async def on_ready():
    print("I'm in")
    print(client.user)

game = game._24()
@tasks.loop(seconds=1.0)
async def delete_grind():
  def check(m):
    return m.channel == game.grind_channel and game.state_grind
  msg = await client.wait_for('message', check=check)
  await msg.delete()

@tasks.loop(seconds=1.0)
async def timer_grind():
  if c(time.time()) > c(game.previous_time) and game.state_grind:
      if not(game.solution_state) :
        await game.message_grind.edit(embed=embed._24.game_grind(game.numbers, c(time.time()) - c(game.start_time), game.score))
      game.previous_time = c(time.time())

@tasks.loop(seconds=1.0)
async def grind_24_checker():
  def check(m):
    return not(game.check(m))
  if game.state_grind:
    print('hi')
    msg = await client.wait_for('message', check = check)
    game.solution_state = True
    await game.message_grind.edit(embed=embed._24.game_grind_correct(game.numbers, game.score, game.score))
    game.generate()
    game.score+=1
    db[f'24-1<@{msg.author.id}>'] += 1
    await asyncio.sleep(0.5)
    game.solution_state = False

@client.command(aliases = ['24', 'twentyfour', 'xxiv', '24 Game', ])
async def game_24(ctx, grind_mode = ''):
    global game
    
    if not(grind_mode) and not(game.state_24) and not(game.state_grind):
      game.generate()
      game.state_24 = True
      await ctx.send(embed=embed._24.game_24(game.numbers))
      def check(m):
        return not(game.check(m))
      msg = await client.wait_for('message', check = check)
      await ctx.send(f'{msg.author} ' + success())
      
      db[f'24-1<@{ctx.author.id}>'] += 1
    elif not(game.state_24) and grind_mode and not(game.state_grind):
      game.grind_channel = ctx.channel
      game.generate()
      game.state_grind = True 
      game.message_grind = await ctx.send(embed=embed._24.game_grind(game.numbers, 0, 0))
      game.start_time = time.time()
      delete_grind.start()
      timer_grind.start()
      grind_24_checker.start()
    else:
      await ctx.send('Game in progress')

    
@client.command(aliases = ['solution', 's'])
async def _solution(ctx):
  if game.state_24:
    await ctx.send(embed=embed._24.solution(game.solution))
    game.state_24 = False
  elif game.state_grind:
    game.solution_state = True
    await game.message_grind.edit(embed=embed._24.game_grind_solution(game.solution, c(time.time()) - c(game.start_time), 0))
    game.generate()
    await asyncio.sleep(2)
    game.solution_state = False
  else:
    await ctx.send('No active game')
  

@client.command(aliases = ['leaderboard','lb'])
async def leaderboard_game(ctx, prefix = '24-1'):
  await ctx.send(embed = leaderboard(prefix))
@client.command(aliases = ['FQ', 'fq', 'f'])
async def quit(ctx):
  global game
  
  game.state_grind = False
  await ctx.send(f'You have quit :(\n You grinded for { c(time.time()) - c(game.start_time)} seconds \n You scored {game.score} points')
  game.score = 0
  game.start_time = 0
  delete_grind.cancel()
  timer_grind.cancel()
  grind_24_checker.cancel()

token = os.environ.get('key')
keep_alive()
client.run(token)