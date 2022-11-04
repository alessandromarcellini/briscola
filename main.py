import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} di {self.suit}"


#40 carte: denari, spade, coppe e bastoni
#da 1 a 10, (prova a mostrare 8, 9 e 10 come fante, cavallo e re
class Deck:
    def __init__(self):
        self.cards = []

    def create(self):
        suits = ["denari", "spade", "coppe", "bastoni"]

        for suit in suits:
            for value in range(1, 11):
                self.cards.append(Card(value, suit))

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
        print(f"Il Bot ha giocato {self.hand[randint]}")
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

        self.cards = []

    def get_briscola(self, deck): #mette la briscola in self.briscola e la sposta dalla cima del mazzo al fondo
        self.briscola = deck.cards.pop()
        deck.cards.append(self.briscola)

    def check_winner(self): #return 1 se vince c2. return 0 se vince c1
        hierarchy = [2, 4, 5, 6, 7, 8, 9, 10, 3, 1]

        if str(self.cards[0].suit) == str(self.briscola) and str(self.cards[1].suit) != str(self.briscola):
            print("\n\n vince il PRIMO ad aver giocato \n\n")
            return 0 #vince il primo ad aver giocato
        elif str(self.cards[1].suit) == str(self.briscola) and str(self.cards[0].suit) != str(self.briscola):
            print("\n\n vince il SECONDO ad aver giocato \n\n")
            return 1 #vince il secondo ad aver giocato
        else: #nessuna delle 2 è briscola o entrambe lo sono
            if str(self.cards[0].suit) != str(self.cards[1].suit):
                print("\n\n vince il PRIMO ad aver giocato \n\n")
                return 0 #vince il primo ad aver giocato
            else: #se hanno stesso seme
                if hierarchy.index(int(self.cards[0].value)) > hierarchy.index(int(self.cards[1].value)):
                    print("\n\n vince il PRIMO ad aver giocato \n\n")
                    return 0 #vince il primo ad aver giocato
                else:
                    print("\n\n vince il SECONDO ad aver giocato \n\n")
                    return 1 #vince il secondo ad aver giocato


    def clean(self):
        return self.cards.clear()

    def display(self):
        player.showHand()
        print("\n-----------\n")
        cpu.showHand()


#creazione giocatori
name = input("Inserisci il tuo NickName: ")
player = Player(name)
cpu = Player("Cpu")

#creazione tavolo
table = Table()

#creazione mazzo
deck = Deck()
deck.create()
deck.shuffle()

print("Buona fortuna!")
#creazione briscola
table.get_briscola(deck)
print(f"La briscola è: {table.briscola}\n")

#creazione mazzo di riferimento, ogni volta che esce una carta la leviamo, teniamo traccia delle carte uscite
reference_deck = Deck()
reference_deck.create()

#CLS, lascia solo la briscola

#iniziare partita, creazione mano giocatori
player.buildHand(deck)
cpu.buildHand(deck)

winner = 0
starting = 0
while len(deck.cards) != 0:
    # mostra mano
    table.display()
    #scegli una carta e mettila sul tavolo
    if winner != 0:
        if starting == 0:
            starting = 1
        else:
            starting = 0

    if starting == 0: #inizia il giocatore
        table.cards.append(player.play())
        table.cards.append(cpu.bot_play()) #logica bot...

    else: #inizia la cpu
        table.cards.append(cpu.bot_play()) #logica bot...
        table.cards.append(player.play())


    #scegli vincitore
    winner = table.check_winner()
    if winner != 0: #ha vinto il secondo a giocare => switch di starting
        if starting == 0: #se era il player a iniziare adesso sarà la cpu
            #pescano
            cpu.draw(deck)
            player.draw(deck)
        else: #se era la cpu a iniziare adesso sarà il player
            #pescano
            player.draw(deck)
            cpu.draw(deck)
    else:
        if starting == 0:
            cpu.draw(deck)
            player.draw(deck)
        else:
            player.draw(deck)
            cpu.draw(deck)

    #assegna punti al vincitore

    #pescare carta



    #riniziare
    table.clean()



#fixato briscola e sistema check winner