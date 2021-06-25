# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
message = ""

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

    def draw_back(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, [pos[0] + CARD_BACK_CENTER[0] + 1, pos[1] + CARD_BACK_CENTER[1] + 1], CARD_BACK_SIZE)

# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards=[]

    def __str__(self):
        # return a string representation of a hand
        name="Hand contains "
        for card in self.cards:
            name=name+str(card)+" "
        return name

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        sum=0
        ace=False
        for card in self.cards:
            sum = sum + VALUES[card.get_rank()]
            if card.get_rank == 'A':
                ace=True
        if not ace:
            return sum
        elif sum+10 <= 21:
            return sum+10
        else:
            return sum

    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for card in self.cards:
            card.draw(canvas,pos)
            pos[0]=pos[0]+CARD_SIZE[0]



# define deck class
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck_of_cards=[]
        for suit in SUITS:
            for rank in RANKS:
                new_card=Card(suit,rank)
                self.deck_of_cards.append(new_card)

    def shuffle(self):
        # shuffle the deck
        # use random.shuffle()
        random.shuffle(self.deck_of_cards)


    def deal_card(self):
        # deal a card object from the deck
        return self.deck_of_cards.pop(0)

    def __str__(self):
        # return a string representing the deck
        name="deck contains "
        for card in self.deck_of_cards:
            name=name+str(card)+" "
        return name



#define event handlers for buttons
def deal():
    global outcome, in_play,player,dealer,curr_deck,message
    # your code goes here
    player=Hand()
    dealer=Hand()
    curr_deck=Deck()
    curr_deck.shuffle()
    message="Hit or Stand?"
    in_play = True
    player.add_card(curr_deck.deal_card())
    player.add_card(curr_deck.deal_card())
    dealer.add_card(curr_deck.deal_card())
    dealer.add_card(curr_deck.deal_card())


def hit():
    # replace with your code below
    global outcome, in_play,player,dealer,curr_deck,score,message
    # if the hand is in play, hit the player
    if in_play:
        player.add_card(curr_deck.deal_card())
    # if busted, assign a message to outcome, update in_play and score
        if player.get_value() > 21:
            outcome=" you have busted!!!"
            score=score-1
            in_play = False
            message="New deal?"
        else:
            message="Hit or Stand?"
        print player
    print outcome

def stand():
    # replace with your code below
    global outcome, in_play,player,dealer,curr_deck,score,message
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(curr_deck.deal_card())
            print dealer

        if dealer.get_value() > 21:
            outcome= "dealer has busted!!!"
            score=score+1
        else:
            if dealer.get_value() >= player.get_value():
                outcome="dealer wins!!"
                score=score-1
            else:
                outcome="player wins!!"
                score=score+1

        message="New deal?"
        in_play=False
    # assign a message to outcome, update in_play and score
    print outcome

# draw handler
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("BLACKJACK", (150, 70), 50, "White")
    canvas.draw_text("dealer", (36, 185), 30, "Black")
    canvas.draw_text("player", (36, 385), 30, "Black")
    canvas.draw_text(outcome, (200,350), 30, "Red")
    canvas.draw_text(message, (200, 400), 30, "Blue")
    canvas.draw_text("Score:" + str(score), (450, 115), 30, "Black")
    dealer.draw(canvas,[100,225])
    player.draw(canvas,[100,425])
    if in_play:
        dealer.cards[0].draw_back(canvas, [100, 225])



# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
