import discord
import os
import json
from keepAlive import keep_alive #connects to http server 
from replit import db
import game #holds 24 Game class which is used for the game 
from message import success 


client = discord.Client()


@client.event
async def on_ready():
    print("I'm in")
    print(client.user)


leaderboard = {}

Game_State = False

game = game._24()
@client.event
async def on_message(message):
    global game
    global Game_State
    global leaderboard
    if message.author != client.user and Game_State == False:
        if message.content == '24 Game':
            game.generate()
            embed = discord.Embed(title=f'Make 24 from {game.numbers}',
                                  description='',
                                  color=0xEB3B45)  # your color in hexadecimal
            await message.channel.send(embed=embed)
            Game_State = True
    if message.content == 'leaderboard':
        with open('leaderboard.txt', 'r') as file:
            leaderboard = (json.load(file))
        lst = []
        sorted_dict = {}
        sorted_keys = sorted(leaderboard, key=leaderboard.get)
        for w in sorted_keys:
            sorted_dict[w] = leaderboard[w]

        big_sign = '--------Leaderboard:--------\n'
        count = len(sorted_dict)
        for j in (sorted_dict):
            lst.append(f'-- {int(count)}. {j} with {sorted_dict[j]} points')
            count -= 1
        lst = lst[::-1]

        big_sign += '\n'.join(lst)
        big_sign += ('\n' + ('-' * 32))
        await message.channel.send(big_sign)

    elif Game_State == True and message.author != client.user:

        if not (game.check(message.content)):

            with open('leaderboard.txt', 'r') as file:
                leaderboard = (json.load(file))
            if f'<@{message.author.id}>' in leaderboard:
                leaderboard[f'<@{message.author.id}>'] += 1
            else:
                leaderboard[f'<@{message.author.id}>'] = 1
            with open('leaderboard.txt', 'w') as file:
                (json.dump(leaderboard, file))
            await message.add_reaction('\N{THUMBS UP SIGN}')

            await message.channel.send(f'{message.author} ' +
                                       success())

            Game_State = False

        elif message.content == 'solution':
            await message.delete()
            embed = discord.Embed(title=f'SOLUTION: {game.solution}', description='', color=0xDB7A35)  # your color in hexadecimal
            await message.channel.send(embed=embed)
            Game_State = False
        elif (game.check(message.content)) == 'no':
            pass
        else:
            await message.channel.send(game.check(message.content))


token = os.environ.get('key')
keep_alive()
client.run(token)
