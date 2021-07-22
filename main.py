import discord
import os
import json
from keepAlive import keep_alive #connects to http server 
from replit import db
import game #holds game classes which r used to initiate games
from message import success 
from leaderboard import leaderboard
import embed
client = discord.Client()


@client.event
async def on_ready():
    print("I'm in")
    print(client.user)



Game_State = False

game = game._24()
@client.event
async def on_message(message):
    global game
    global Game_State
    if message.author != client.user and Game_State == False:
        if message.content == '24 Game':
            game.generate()
            await message.channel.send(embed=embed._24.game_24(game.numbers))
            Game_State = True
    if message.content == 'leaderboard':
        await message.channel.send(embed = leaderboard('24-1'))
    elif Game_State == True and message.author != client.user:

        if not (game.check(message.content)):
            db[f'24-1<@{message.author.id}>'] += 1

            await message.channel.send(f'{message.author} ' + success())

            Game_State = False

        elif message.content == 'solution':
            await message.delete()
            await message.channel.send(embed=embed._24.solution(game.solution))
            Game_State = False
        elif (game.check(message.content)) == 'no':
            pass
        else:
            await message.channel.send(game.check(message.content))


token = os.environ.get('key')
keep_alive()
client.run(token)
