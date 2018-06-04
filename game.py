from minigame import MindNumber

md = MindNumber()

def new_game(d):
    md.newGame()
    return {'code':'success'}

def guess(d):
    try:
        guess = d.get('guess', [''])[0]
    except:
        return {'code':'error', 'msg':'wrong guess parameter'}
    userGuess = md.guess(guess)
    trials = md.getGuessCount()

    return {'code':'success', 'userGuess':userGuess, 'trials': trials}



