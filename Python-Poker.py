import random
import time
names = ['John','Dave','Norm','Charles','Hank','Eric','Shaw','']
deck=['A.S','K.S','Q.S','J.S','2.S','3.S','4.S','5.S','6.S','7.S','8.S','9.S','10.S',
        'A.C','K.C','Q.C','J.C','2.C','3.C','4.C','5.C','6.C','7.C','8.C','9.C','10.C',
        'A.H','K.H','Q.H','J.H','2.H','3.H','4.H','5.H','6.H','7.H','8.H','9.H','10.H',
        'A.D','K.D','Q.D','J.D','2.D','3.D','4.D','5.D','6.D','7.D','8.D','9.D','10.D',]

player1Hand = []
player2Hand = []
player3Hand = []

random.shuffle(deck)

class playerAI:

    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def dealCards(self):
        self.hand.append(deck[0])
        # self.hand.remove(deck[0])
        print(self.name, self.hand)


def generatePlayers():
    #creates player 1
    player1Name  = random.choice(names)
    player1 = playerAI(player1Name, player1Hand)
    player1.dealCards()

    #creates player 2
    player2Name  = random.choice(names)
    player2 = playerAI(player2Name, player2Hand)
    player2.dealCards()

    #creates player 3
    player3Name  = random.choice(names)
    player3 = playerAI(player3Name, player3Hand)
    player3.dealCards()


def main():
    generatePlayers()



if __name__ == '__main__':
    main()