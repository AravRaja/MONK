def generate_message():  #generates success message
    from random import randint as r
    responces = [
        'You Genius', 'Play it again, Sam', 'Darn', 'no need to show off',
        'we rise', 'why?', '<3', 'Frankly, my dear, I dont give a damn.',
        'Just keep swimming.', 'You is kind. You is smart. You is important.',
        'You talking to me?'
    ]
    return responces[r(0, len(responces) - 1)]