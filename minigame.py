import random
class MindNumber:
    def __init__(self):
        self.secret = 0
        self.trials = 0
    def newGame(self):
        self.secret = random.randint(1,1000)
        self.trials = 0
    def guess(self,userGuess):
        self.trials += 1
        if userGuess > self.secret:
            print("Smaller")
        elif userGuess < self.secret:
            print("Greater")
        return userGuess
    def getGuessCount(self):
        return self.trials
if __name__ == '__main__':
    m = MindNumber()
    m.newGame()
    s = m.secret
    n = 0
    while n != s:
        inputString = int(input("Your guess: "))
        n = m.guess(inputString)
    guessCount = m.getGuessCount()
    print("SUCCESS in %d tries"%(guessCount))

