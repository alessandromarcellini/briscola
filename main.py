import random

class Card:
    def __init__(self, valore, seme):
        self.valore = valore
        self.seme = seme

    def __str__(self):
        return f"{self.valore} di {self.seme}"


#40 carte: denari, spade, coppe e bastoni
#da 1 a 10, (prova a mostrare 8, 9 e 10 come fante, cavallo e re
class Deck:
    def __init__(self):
        self.cards = []

    def create(self):
        semi = ["denari", "spade", "coppe", "bastoni"]

        for seme in semi:
            for valore in range(1, 11):
                self.cards.append(Card(valore, seme))

    def showDeck(self):
        for card in self.cards:
            print(card)

    #carta, scambiane la posizione con una precedente
    #parti dal fondo, randint(:i)
    def shuffle(self):
        #parti dal fondo
        for i in range(39, -1, -1):
            #genera un int random < i
            randint = random.randint(0, i)
            #scambia la i-esima carta con quella di posizione randint
            if randint != i:
                self.cards[i], self.cards[randint] = self.cards[randint], self.cards[i]

    #leva la carta in cima al mazzo, (l'ultima della lista)
    def pop(self):
        return self.cards.pop()

class Player:
    def __init__(self, name, points=0):
        self.name = name #giocatore o cpu
        self.points = points

        self.hand = [] #da massimo 3 carte

    def buildHand(self, deck):
        for i in range(3):
            self.hand.append(deck.pop())

    def play(self):
        index = int(input("Inserisci il numero della carta da giocare (1-3): "))
        if index <= 3 and index >=1:
            return self.hand.pop(index - 1)
        else:
            raise ValueError('Il numero della carta da giocare deve essere compreso tra 1 e 3!')

    def bot_play(self):
        randint = random.randint(0, 2)
        return self.hand.pop(randint)

    def draw(self, deck):
        self.hand.append(deck.pop())

    #mostra mano al giocatore
    def showHand(self):
        print(str(self.name) + ":")
        for i in range(len(self.hand)):
            print(self.hand[i])

class Table:
    def __init__(self):
        semi = ["denari", "spade", "coppe", "bastoni"]

        self.cards = []
        self.briscola = semi[random.randint(0, 3)]



#creazione giocatori
name = input("Inserisci il tuo NickName: ")
player = Player(name)
cpu = Player("Cpu")

#creazione tavolo
table = Table()
print("Buona fortuna!")
print(f"La briscola è: {table.briscola}\n")


#creazione mazzo
deck = Deck()
deck.create()
deck.shuffle()

#creazione mazzo di riferimento, ogni volta che esce una carta la leviamo, teniamo traccia delle carte uscite
reference_deck = Deck()
reference_deck.create()

#CLS, lascia solo la briscola

#iniziare partita, creazione mano giocatori
player.buildHand(deck)
cpu.buildHand(deck)

while len(deck.cards) != 0:
    # mostra mano
    player.showHand()
    print("\n-----------\n")
    cpu.showHand()


    #scegli una carta e mettila sul tavolo
    table.cards.append(player.play())

    #logica bot...
    table.cards.append(cpu.bot_play())

    #scegli vincitore


    #assegna punti al vincitore

    #pescare carta

    #riniziare

