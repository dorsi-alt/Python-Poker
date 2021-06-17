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
player4Hand = []

random.shuffle(deck)

def playerAction():
    print("What Action Would You Like To Perform")
    print("1. Call")
    print("2. Raise")
    print("3. Check")
    print("4. Fold")


class playerAI:
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

def generatePlayers():
    #creates player 1
    player1Name  = random.choice(names)
    player1 = playerAI(player1Name, player1Hand)


    #creates player 2
    player2Name  = random.choice(names)
    player2 = playerAI(player2Name, player2Hand)

    #creates player 3
    player3Name  = random.choice(names)
    player3 = playerAI(player3Name, player3Hand)


class Table:
    def __init__(self,p1hand,p2hand,p3hand,p4hand):
        self.players = 4
        self.p1hand = p1hand
        self.p2hand = p2hand
        self.p3hand = p3hand
        self.p4hand = p4hand
        self.deck = deck
    
    def dealHands(self):
        #loops for both cards in a hand 
        for x in range (2):
            #adds cards to first players hand and removes the card from the deck 
            self.p1hand.append(deck[0])
            deck.remove(deck[0])

            #adds cards to second players hand and removes the card from the deck 
            self.p2hand.append(deck[0])
            deck.remove(deck[0])
        
            #adds cards to third players hand and removes the card from the deck 
            self.p3hand.append(deck[0])
            deck.remove(deck[0])

            #adds cards to forth players hand and removes the card from the deck 
            self.p4hand.append(deck[0])
            deck.remove(deck[0])

        print(self.p1hand)
        print(self.p2hand)    
        print(self.p3hand)
        print(self.p4hand)

def generateTable():
    Table1 = Table(player1Hand,player2Hand,player3Hand,player4Hand)
    Table1.dealHands()




def main():
    generatePlayers()
    generateTable()



if __name__ == '__main__':
    main()