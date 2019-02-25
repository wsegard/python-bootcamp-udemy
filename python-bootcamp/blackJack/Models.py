import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

#************* Card Model ****************

class Card:

  def __init__(self, suit, rank):
    self.suit = suit
    self.rank = rank

  def __str__(self):
    return "%s of %s" %(self.rank, self.suit)


#************* Deck Model ****************

class Deck:

  def __init__(self):
    self.deck = []
    for suit in suits:
      for rank in ranks:
        self.deck.append(Card(suit, rank))

  def __str__(self):
    deck_comp = ''
    for i in self.deck:
      deck_comp += "\n " + str(i)
    return "The deck has:" + deck_comp

  def shuffle(self):
    return random.shuffle(self.deck)

  def deal(self):
    single_card = self.deck.pop()
    return single_card

#************* Hand Model ****************

class Hand:

  def __init__(self):
      self.cards = []
      self.value = 0
      self.aces = 0

  def __str__(self):
    hand_comp = ''
    for i in self.cards:
      hand_comp += "\n " + str(i)
    return "Your hand is:" + hand_comp

  def add_card(self, card):
    self.cards.append(card)
    self.value += values[card.rank]
    if card.rank == "Ace":
      self.aces += 1

  def adjust_for_ace(self):
    if self.value > 21 and self.aces > 0:
      self.value -= 10
      self.aces -= 1

#************* Chips Model ****************

class Chips:

  def __init__(self,total = 100):
    self.total = total
    self.bet = 0

  def win_bet(self):
    self.total += self.bet

  def lose_bet(self):
    self.total -= self.bet

#************* Take bet ****************

def take_bet(chips):
  while True:
    try:
      chips.bet = int(input("How much do you want to bet? "))
    except ValueError:
      print("Please enter an integer!")
      continue
    else:
      if chips.bet > chips.total:
        print("You can't bet more than %s" %(chips.total))
      else:
        break

def hit(deck, hand):
  hand.add_card(deck.deal())
  hand.adjust_for_ace()

def hit_or_stand(deck, hand):
  global playing
  while True:
    try:
      next_play = input("What's your next play: 'hit' or 'stand'? ").lower()
    except:
      print("I did not understand what you want to do!")
    else:
      if next_play == 'hit' or next_play == 'stand':
        break
  if next_play == 'hit':
    hit(deck, hand)
  else:
    print("Player stands. Dealer is playing.")
    playing = False

def show_some(player,dealer):
  print("\nDealer's Hand:")
  print(" <card hidden>")
  print(str(dealer.cards[1]))
  #print("\nPlayer's Hand:", *player.cards, sep='\n ')
  print("\nPlayer's Hand:")
  for i in player.cards:
    print(str(i))

def show_all(player,dealer):
  #print("\nDealer's Hand:", *dealer.cards, sep='\n ')
  #print("Dealer's Hand =",dealer.value)
  #print("\nPlayer's Hand:", *player.cards, sep='\n ')
  #print("Player's Hand =",player.value)
  print("\nDealer's Hand:")
  for i in dealer.cards:
    print(str(i))
  print("\nPlayer's Hand:")
  for i in player.cards:
    print(str(i))






def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! It's a push.")



print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
Dealer hits until she reaches 17. Aces count as 1 or 11.')
player_chips = Chips()

while True:
  #initialize
  deck = Deck()
  deck.shuffle()

  player_hand = Hand()
  dealer_hand = Hand()
  player_hand.add_card(deck.deal())
  dealer_hand.add_card(deck.deal())
  player_hand.add_card(deck.deal())
  dealer_hand.add_card(deck.deal())

  take_bet(player_chips)

  show_some(player_hand,dealer_hand)

  while playing:
    print('\n')
    hit_or_stand(deck, player_hand)
    show_some(player_hand,dealer_hand)
    if player_hand.value > 21:
      print('\n')
      player_busts(player_hand,dealer_hand,player_chips)
      break

  if player_hand.value <= 21:
    while dealer_hand.value < 17 or dealer_hand.value <= player_hand.value:
      print("\n")
      hit(deck, dealer_hand)
    show_all(player_hand, dealer_hand)
    print("\n")
    if dealer_hand.value > 21:
      dealer_busts(player_hand,dealer_hand,player_chips)
    elif dealer_hand.value > player_hand.value:
      dealer_wins(player_hand,dealer_hand,player_chips)
    elif dealer_hand.value < player_hand.value:
      player_wins(player_hand,dealer_hand,player_chips)
    else:
      push(player_hand,dealer_hand)

# Inform Player of their chips total
  print("\n")
  print("Player's winnings stand at",player_chips.total)

    # Ask to play again
  print("\n")
  new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

  if new_game[0].lower()=='y':
    playing=True
    continue
  else:
    print("Thanks for playing!")
    break








