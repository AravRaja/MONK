def leaderboard(p):
        import discord
        from replit import db 
        tupl = db.prefix(p)
        leaderboard = {i:db[i] for i in tupl}
        
        lst = []
        sorted_dict = {}
        sorted_keys = sorted(leaderboard, key=leaderboard.get)
        for w in sorted_keys:
            sorted_dict[w] = leaderboard[w]
        sign = '--------Leaderboard:--------\n'
        big_sign = ''
        count = len(sorted_dict)
        for j in (sorted_dict):
            lst.append(f'-- ***{int(count)}.*** {j[4:]}  with `{sorted_dict[j]}`  points')
            count -= 1
        lst = lst[::-1]

        big_sign += '\n'.join(lst)
        big_sign += ('\n' + '***'+ '-'*32+ '***')
        big_sign = discord.Embed(title = sign, description = big_sign, color= 0x121212)
        return big_sign
