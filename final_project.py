
Player = raw_input ("Player name: ")

master_card_deck = ["A spades", "A diamonds", "A clubs", "A hearts", "J spades", "Q spades", "K spades", "J hearts", "Q hearts", "K hearts", "J diamonds", "Q diamonds", "K diamonds", "J clubs", "Q clubs", "K clubs", "2 spades", "3 spades", "4 spades", "5 spades", "6 spades", "7 spades", "8 spades", "9 spades", "10 spades", "2 hearts", "3 hearts", "4 hearts", "5 hearts", "6 hearts", "7 hearts", "8 hearts", "9 hearts", "10 hearts", "2 diamonds", "3 diamonds", "4 diamonds", "5 diamonds", "6 diamonds", "7 diamonds", "8 diamonds", "9 diamonds", "10 diamonds", "2 clubs", "3 clubs", "4 clubs", "5 clubs", "6 clubs", "7 clubs", "8 clubs", "9 clubs", "10 clubs"]
card_deck = list(master_card_deck)

import random
import time

def shuffle_hand():
# shuffles card deck
	shuffle = raw_input("Shuffle cards? y/n ")
	if (shuffle == 'y'):
		random.shuffle(card_deck)

dealer = [card_deck[0], card_deck[1]]
player_hand = [card_deck[2], card_deck[3]]
# draws hand for dealer & player

def card_add1(hand):
# Adds the cards in the dealer's hand - taking Aces into consideration.
# When sum is more than 11, Ace is worth 1, Sum is less than 11, Ace is worth 11
	hand.sort()
	index = 0
	sum = 0
	add = 0
	for card in hand:
		value = (card.split(" ")[0])
		if value == "J" or value == "Q" or value == "K":
			add = 10
		elif value == "A":
			if sum >= 11:
				add = 1
			else:
				add = 11
		else:
			add = int(card.split(" ")[0])
		sum = sum + add
	return sum

def card_add2(hand):
# Adds the cards in the player's hand - taking Aces into consideration.
# Player has the option to select Ace to be 1 or 11 - and change these values as the hand unfolds.
	hand.sort()
	index = 0
	sum = 0
	add = 0
	for card in hand:
		value = (card.split(" ")[0])
		if value == "J" or value == "Q" or value == "K":
			add = 10
		elif value == "A":
			ace_value = raw_input("\nAce value 1 or 11? ")
			if ace_value == "1":
				add = 1
			else:
				add = 11
		else:
			add = int(card.split(" ")[0])
		sum = sum + add
	return sum	

def deal_hand():
# Displays the first card for the dealer
# Displays both cards for the player & calculates total
		print "\nDealer Hand:"
		print dealer[0]
		time.sleep(2)
		print "\n%s's Hand:" % (Player)
		for x in player_hand:
			print x,
		player_hand_total = card_add2(player_hand)
		print "\nTotal: ", player_hand_total

		del card_deck[0:4]

def continue_player_hand():	
# Lets the player decide whether to take more cards or to stand.  Uses card_add2 function to allow Aces to be reassigned as needed.
# Continues until player decides to stand, or hand is bust	
	player_hand_total = 0
	while True:
		extra_card = raw_input("\nHit? y/n ")
		if extra_card == 'y':
			print "\n%s's hand:" % (Player)
			time.sleep(1)
			player_hand.append(card_deck[0]) # adds next card to the hand - displayed & totaled)
			for x in player_hand:
				print x,
			player_hand_total = card_add2(player_hand)
			print "\nTotal: ", player_hand_total
			del card_deck[0] # need to delete as otherwise same card keeps being drawn
			if player_hand_total > 21:
				print "\nBust!\n"
				time.sleep(1)
				break
		else:
			if player_hand_total == 0:
				player_hand_total = card_add2(player_hand)
			print "Stand Total: ", player_hand_total
			time.sleep(1)
			break
	return player_hand_total

def continue_dealer_hand(ptotal):
# Plays the dealer's hand.  Displays both dealer cards.  While the dealer's hand is under 17, another card will continue to be drawn.
# When dealer hand above 17, dealer stands.
# If dealer's hand goes above 21, dealer is bust.
	dealer_hand_total = card_add1(dealer)
	print "\nDealer Hand:"
	for x in dealer:
		print  x,
	print "\nTotal: ", dealer_hand_total
	time.sleep(2)
	while True:
		dealer_hand_total = card_add1(dealer)
		if (dealer_hand_total < 17) and (ptotal < 22):
			print "\n\nDealer draws another card:"
			dealer.append(card_deck[0]) # adds next card to the hand - displayed & totaled
			dealer_hand_total = card_add1(dealer)
			for x in dealer:
				print x, 
			print "\nTotal: ", dealer_hand_total
			del card_deck[0] # need to delete, else same card keeps being drawn
			time.sleep(2)
		elif dealer_hand_total > 21:
			print "\nTotal: ", dealer_hand_total
			print "\nDealer Bust!"
			time.sleep(1)
			break
		else:
			if dealer_hand_total == 0:
				dealer_hand_total = card_add1(dealer)
			print "\nTotal: ", dealer_hand_total
			time.sleep(1)
			break
	return dealer_hand_total

def winner(player_hand_total, dealer_hand_total):
# Calculates winner of game
	if (22 > player_hand_total > dealer_hand_total):
		print "\nGame over! %s Wins!" % (Player)
	elif card_add1(dealer) > 21:
		print "\nGame over! %s Wins!" % (Player)
	elif card_add1(player_hand) > 21:
		print "\nGame over! Dealer wins!" 
	elif (dealer_hand_total > player_hand_total):
		print "\nGame over! Dealer Wins!" 
	else:
		print "\nGame Tied - No winner!" 

def new_game():
# Function to run the game.  Can keep selecting to play without needing to re-enter name.
	ask_new_game = raw_input("\nNew Game? y/n ")
	if ask_new_game == 'y':
		shuffle_hand()
		del dealer[:]
		del player_hand[:]
		dealer.extend([card_deck[0], card_deck[1]])
		player_hand.extend([card_deck[2], card_deck[3]])
		ask_deal_hand = raw_input ("Deal Hand? y/n ")
		if ask_deal_hand == 'y':
			deal_hand()
			player_hand_total = continue_player_hand()
			dealer_hand_total = continue_dealer_hand(player_hand_total)
			winner(player_hand_total, dealer_hand_total)
			new_game()
		else: 
			print "End of Game"
	else:
		print "End of Game"

new_game()
