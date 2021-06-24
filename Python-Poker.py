import random
import time
names = ['John','Dave','Norm','Charles','Hank','Eric','Shaw','Mike','Kevin','Jane','Monica','Racheal','Pheobe','Janice','Jenn','Katherine']

deck=['A.S','K.S','Q.S','J.S','2.S','3.S','4.S','5.S','6.S','7.S','8.S','9.S','10.S',
        'A.C','K.C','Q.C','J.C','2.C','3.C','4.C','5.C','6.C','7.C','8.C','9.C','10.C',
        'A.H','K.H','Q.H','J.H','2.H','3.H','4.H','5.H','6.H','7.H','8.H','9.H','10.H',
        'A.D','K.D','Q.D','J.D','2.D','3.D','4.D','5.D','6.D','7.D','8.D','9.D','10.D',]


tableMaxSize = 4
potSize = 0
player1Money = 1000
player2Money = 1000
player3Money = 1000
userMoney = 1000
playerMoneyArray = [player1Money,player2Money,player3Money,userMoney]
middleCards = []
publicTableList = []
player1Hand = []
player2Hand = []
player3Hand = []
userHand = []
playerList = []




random.shuffle(deck)

class user:

    def __init__(self,name, hand, money):
        self.name = name
        self.hand = hand
 
    def displayCards(self):
        print(self.name, self.hand)

class playerAI:

    def __init__(self,name,hand,money):
        self.name = name
        self.hand = hand
        self.money = money

    def bet(self):
        time.sleep(1)
        (self.name, " is make his decision...")
    
    def displayCards(self):
        print(self.name,"?,?")

    def makebet():
        pass

class Table:

    def __init__(self, name, p1hand, p2hand, p3hand, p4hand, seats, publicTableList, middleCards):
        self.name = name
        self.seats = seats
        self.p1hand = p1hand
        self.p2hand = p2hand
        self.p3hand = p3hand
        self.p4hand = p4hand
        self.playerList = playerList
        self.publicList = publicTableList
        self.middleCards = middleCards

    def setPlayers(self):

        self.playerList.append()

    def setStatus(self):
            self.publicList.append(self.name)

    def playerJoined(self):
        self.seat -= 1
        print(self.seats)
        return(self.seats)

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

            self.p4hand.append(deck[0])
            deck.remove(deck[0])

    def dealFlop(self):
        self.middleCards.append(deck[0])
        deck.remove(deck[0])
        
        self.middleCards.append(deck[0])
        deck.remove(deck[0])

        self.middleCards.append(deck[0])
        deck.remove(deck[0])
        
        print(self.middleCards)

    def dealTurn(self):
        print("Dealing Turn...")
        self.middleCards.append(deck[0])
        deck.remove(deck[0])
        print(self.middleCards)

    def dealRiver(self):
        print("Revealing River...")
        self.middleCards.append(deck[0])
        deck.remove(deck[0])
        print(self.middleCards)


def Title():
    global userName
    print("WELCOME TO TEXAS POKER!")
    time.sleep(1.5)
    userName = input("What Is Your Name:\n")
    time.sleep(1.5)
    return userName


def initGame():

    Title()
    #generates table object
    Table1 = Table("danielsTable", player1Hand, player2Hand, player3Hand, userHand, tableMaxSize, publicTableList, middleCards)
    Table1.setStatus()
    

    #creates player 1
    player1Name  = random.choice(names)
    player1 = playerAI(player1Name, player1Hand,player1Money)


    #creates player 2
    player2Name  = random.choice(names)
    player2 = playerAI(player2Name, player2Hand,player2Money)


    #creates player 3
    player3Name  = random.choice(names)
    player3 = playerAI(player3Name, player3Hand,player3Money)


    person = user(userName, userHand,userMoney)

    playerList = [player1,player2,player3,person]


    Table1.dealHands()
    player1.displayCards()
    player2.displayCards()
    player3.displayCards()
    person.displayCards()
    Table1.dealFlop()
    Table1.dealTurn()
    Table1.dealRiver()

    




def main():
    initGame()



if __name__ == '__main__':
    main()
