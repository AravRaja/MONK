import discord

class _24:
  
  def solution(solution):
    embed = discord.Embed(title=f'SOLUTION: {solution}', description='', color= 0xEB3B45)
    return embed
  def game_24(numbers):
    written = [':zero:', ':one:', ':two:', ':three:', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:', ':keycap_ten:','<:eleven:870420155925164052>','<:twelve:870419944226062406>', '<:thirteen:870419721604984892>']
    emoji =''
    for i in numbers:
      emoji+= written[i]+' '


    
    embed = discord.Embed(title=f'Make 24 from: {emoji}', description='', color= 0xEA4B45) 
    return embed
  def game_grind(numbers, timer, score):
    written = [':zero:', ':one:', ':two:', ':three:', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:', ':keycap_ten:','<:eleven:870420155925164052>','<:twelve:870419944226062406>', '<:thirteen:870419721604984892>']
    emoji =''
    for i in numbers:
      emoji+= written[i]+' '
    embed=discord.Embed(title=f"{1*'<:embed:870442477922975856>'}Make 24 from: {emoji}", description=f"**----------------------------------------------**\n\n{'<:thin_embed:870446527364071454>'*0}:clock{timer%12+1}: : `{timer}`{'<:embed:870442477922975856>'*2}:third_place: : `{score}`{'<:embed:870442477922975856>'*2}:x: : `FQ` " , color=0xa421d4)
    embed.set_author(name="----------------------------------------------")
    

    return embed
  def game_grind_correct(numbers, timer,score):
        
    written = [':zero:', ':one:', ':two:', ':three:', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:', ':keycap_ten:','<:eleven:870420155925164052>','<:twelve:870419944226062406>', '<:thirteen:870419721604984892>']
    emoji =''
    for i in numbers:
      emoji+= written[i]+' '
    embed=discord.Embed(title=f"{1*'<:embed:870442477922975856>'} CORRECT :tick: `+1`", description=f"**----------------------------------------------**\n\n{'<:thin_embed:870446527364071454>'*0}:clock{timer%12+1}: : `{timer}`{'<:embed:870442477922975856>'*2}:third_place: : `{score}`{'<:embed:870442477922975856>'*2}:x: : `FQ` " , color=0x34eb3a)
    embed.set_author(name="----------------------------------------------")
    return embed
  def game_grind_solution(solution, timer,score):
        
    written = [':zero:', ':one:', ':two:', ':three:', ':four:', ':five:', ':six:', ':seven:', ':eight:', ':nine:', ':keycap_ten:','<:eleven:870420155925164052>','<:twelve:870419944226062406>', '<:thirteen:870419721604984892>']
    emoji =''
 
    embed=discord.Embed(title=f"{1*'<:embed:870442477922975856>'} SOLUTION `{solution}`", description=f"**----------------------------------------------**\n\n{'<:thin_embed:870446527364071454>'*0}:clock{timer%12+1}: : `{timer}`{'<:embed:870442477922975856>'*2}:third_place: : `{score}`{'<:embed:870442477922975856>'*2}:x: : `FQ` " , color=0xf1f500)
    embed.set_author(name="----------------------------------------------")
    

    return embed