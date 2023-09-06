# -*- coding: utf-8 -*-
"""
Rules:
Try to get as close to 21 without going over.
Kings, Queens, and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet
but must hit exactly one more time before standing.
In case of a tie, the bet is returned to the player.
The dealer stops hitting at 17.
"""
import random
from copy import deepcopy 

HEARTS = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES = chr(9824) # Character 9824 is '♠'.
CLUBS = chr(9827) # Character 9827 is '♣'.

class Card:
    def __init__(self,value,suit):
        self.value=value
        self.suit=suit
        
    def __repr__(self):
        return f'{self.value} of {self.suit}'

DECK=[Card(value,suit) for value in 'A 2 3 4 5 6 7 8 9 10 K Q J'.split()
      for suit in [HEARTS, DIAMONDS, SPADES, CLUBS]]

def display_cards(cards,hole_card):
    '''   ___
         |2  |
         | ♥ |
         |__2|'''

    
    list_of_cards=deepcopy(cards)
    
    if hole_card:
        list_of_cards[0].value, list_of_cards[0].suit = '#', '#'         
        
    first_line=[' ___' for card in list_of_cards]
    second_line=['|{0:3}|'.format(card.value) for card in list_of_cards]
    third_line=[f'| {card.suit} |' for card in list_of_cards]
    fourth_line=['|_{0:>2}|'.format(card.value) for card in list_of_cards]
    
    lines=['   '.join(first_line),'  '.join(second_line), '  '.join(third_line),
           '  '.join(fourth_line)]
    
    return '\n'.join(lines)
    
def draw_card(deck):
    card=random.choice(deck)
    deck.remove(card)
    return card

def get_score(cards,hole_card=False):    
    if hole_card:
        return '???'
    
    else:        
        score=0
        has_ace=False       
        for card in cards:
            if card.value == 'A': # the value of the first ace will be determined at the end
                if has_ace: score+=1
                else: has_ace=True
                    
            if card.value in '2 3 4 5 6 7 8 9 10'.split(): score+=int(card.value) 
            
            if card.value in 'QJK': score+=10
            
        if has_ace: # scores the first Ace (if there's more than one, they're scored 1)
            if score+11>21: score+=1
            else: score+=11
        
        return score

def print_table(player_cards,dealer_cards,hole_card):
    
    print(f'\nDealer: {get_score(dealer_cards,hole_card)}')
    print(display_cards(dealer_cards,hole_card))
    
    print(f'\nPlayer: {get_score(player_cards,False)}')
    print(display_cards(player_cards,False))
                    
def game(money):  
    
    print(f'\nMoney: {money}')
    
    bet=input(f'How much do you bet? (1-{money}, or quit)\n> ')
    
    if bet.lower().startswith('q'): 
        print('Ok, bye!')
        return (False,money)
    
    deck=[Card(value,suit) for value in 'A 2 3 4 5 6 7 8 9 10 K Q J'.split()
          for suit in [HEARTS, DIAMONDS, SPADES, CLUBS]]
    random.shuffle(deck)
    
    player_cards=[]
    dealer_cards=[] 

    player_isplaying=True

    # draw 2 cards for each one 
    print(f'Bet: {bet}')
    player_cards.append(draw_card(deck))
    player_cards.append(draw_card(deck))
    dealer_cards.append(draw_card(deck))
    dealer_cards.append(draw_card(deck)) 

    print('\nTurn #1')       
    print_table(player_cards, dealer_cards,hole_card=True)
    
    first_play=True
    turn = 2
    while player_isplaying or get_score(dealer_cards)<17:
        
        if get_score(player_cards)>=21: player_isplaying=False
        
        print(f'\nTurn #{turn}')
        
        # player's turn
        if player_isplaying:
            
            if first_play:
                play=input('\n(H)it, (S)tand, (D)ouble down\n> ')
                first_play=False
            else: play=input('\n(H)it, (S)tand\n> ')
            
            if  play.lower().startswith('d'):
                new_card=draw_card(deck)
                player_cards.append(new_card)
                print(f'You drew a {new_card}')
                player_isplaying=False
                
            if play.lower().startswith('h'):
                new_card=draw_card(deck)
                player_cards.append(new_card)
                print(f'You drew a {new_card}')
                
            if play.lower().startswith('s'):
                print('You chose to stand.')
                player_isplaying=False
                            
            
        # dealer's turn
        
        if get_score(dealer_cards)<=17:
            dealer_cards.append(draw_card(deck))
            
        # show table
        
        print_table(player_cards, dealer_cards, player_isplaying) # hole card if the player is still playing
        
        turn+=1
    # who is the winner

    player_score = get_score(player_cards)
    dealer_score = get_score(dealer_cards)
    
    if player_score==21 or dealer_score>21:
        money+=int(bet)
        print('\nYou won!')
        return (True, money)
        
    if player_score>21:
        money-=int(bet)
        print('\nYou lost.')
        return (True, money)  
    
    if max(player_score,dealer_score)==player_score:
        money+=int(bet)
        print('\nYou won!')
    else:
        money-=int(bet)
        print('\nYou lost.')        
    
    return (True, money)   
 
def main():
    
    print('''
          Blackjack, by Renato Maia.
          
          Rules:
          Try to get as close to 21 without going over.
          Kings, Queens, and Jacks are worth 10 points.
          Aces are worth 1 or 11 points.
          Cards 2 through 10 are worth their face value.
          (H)it to take another card.
          (S)tand to stop taking cards.
          On your first play, you can (D)ouble down to increase your bet
          but must hit exactly one more time before standing.
          In case of a tie, the bet is returned to the player.
          The dealer stops hitting at 17.''')
    
    money=5000
    wanna_play=True
    
    while wanna_play and money>0:
        
        output=game(money)
        wanna_play=output[0]
        money=output[1]
        
    print('Thanks for playing :)')   

if __name__=='__main__':
    main() 
