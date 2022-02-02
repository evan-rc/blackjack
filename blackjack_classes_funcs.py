import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10 , 'Ace':1}
disp_values = {'Two':'2 ','Three':'3 ','Four':'4 ',
           'Five':'5 ','Six':'6 ','Seven':'7 ',
           'Eight':'8 ','Nine':'9 ','Ten':'10',
          'Jack':'J ','Queen':'Q ','King':'K ',
          'Ace':'A '}
disp_suits = {'Hearts':'♥︎','Diamonds':'♦︎','Spades':'♠︎','Clubs':'♣︎'}

class Card:
    '''a card class'''
    def __init__(self, suit, rank, visible = True):
        '''initializes card class with suit, rank, value, display value, visibility, and display suit attributes'''
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        self.disp_value = disp_values[rank]
        self.visible = visible
        self.disp_suit = disp_suits[suit]
        
    def __str__(self):
        '''retuns card string with rank and suit'''
        return self.rank + ' of ' + self.suit
        
    def flip(self):
        '''flips whether card is visible'''
        if self.visible == True:
            self.visible = False
        else:
            self.visible = True

class Deck:
    '''a deck class'''
    def __init__(self):
        '''makes a deck of cards using the Card class'''
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                new_card = Card(suit,rank,True)
                self.all_cards.append(new_card)
                
    def deal_one(self):
        '''removes and returns one card from the deck'''
        return self.all_cards.pop()
    
    def shuffle(self):
        '''shuffles the entire deck'''
        random.shuffle(self.all_cards)
        
    def __len__(self):
        '''returns the number of cards in the deck'''
        return len(self.all_cards)

    def combine(self,adl_deck):
        '''adds an additional deck to this deck'''
        self.all_cards = self.all_cards + adl_deck.all_cards

class Table:
    '''a table class'''
    def __init__(self):
        self.pot = 0
        self.pot2 = 0
        self.discard_pile = []
        
    def add_discard(self,new_card):
        '''adds a card to the discard pile'''
        self.discard_pile.append(new_card)
        
    def remove_discard(self):
        '''removes a card from the discard pile'''
        # NEEDS TO BE IMPLEMENTED
        '''will be used to reshuffle deck'''
        return self.discard_pile.pop()
    
    def add_pot(self,amount,ispot2 = False):
        '''adds an amount to a pot'''
        '''can take in if its a split pot as boolean and add it to the second pot'''
        if ispot2 == False:
            self.pot = self.pot + amount
        if ispot2 == True:
            self.pot2 = self.pot2 + amount
        
    def remove_pot(self,amount):
        '''takes in an amount and removes it from the pot'''
        self.pot = self.pot - amount
        
    def display_pot(self):
        '''displays just the pot'''
        print(f'POT: ${self.pot}')
        
    def print_cards(self, cards):
        '''prints cards'''
        s = ''
        i = 0
        for card in cards:
            s = s + '\t ___________'
        print (s)
        s = ''
        for card in cards:

            if card.visible is True:
                s = s + '\t|           |'
            if card.visible is False:
                s = s + '\t| _________ |'

        print (s)
        s = ''

        for card in cards:
            if card.visible is True:
                s = s + '\t|  ' +f'{card.disp_value}' + '       |'
            if card.visible is False:
                s = s + '\t||/////////||'
        print (s)
        s = ''

        for card in cards:
            if card.visible is True:
                s = s + '\t|           |'
            if card.visible is False:
                s = s + '\t||/////////||'
        print (s)
        s = ''

        for card in cards:
            if card.visible is True:
                s = s + '\t|           |'
            if card.visible is False:
                s = s + '\t||/////////||'
        print(s)
        s = ''
        for card in cards:
            if card.visible is True:
                s = s + '\t|     ' + f'{card.disp_suit}' + '     |'
            if card.visible is False:
                s = s + '\t||/////////||'
        print (s)
        s = ''

        for card in cards:
            if card.visible is True:
                s = s + '\t|           |'
            if card.visible is False:
                s = s + '\t||/////////||'
        print(s)
        s = ''

        for card in cards:
            if card.visible is True:
                s = s + '\t|           |'
            if card.visible is False:
                s = s + '\t||/////////||'
        print(s)
        s = ''
        for card in cards:
            if card.visible is True:
                s = s + '\t|        ' +f'{card.disp_value}' + ' |'
            if card.visible is False:
                s = s + '\t||'+'\033[4m/////////\033[0m'+'||'
        print (s)
        s = ''
        for card in cards:
            s = s + '\t|___________|'
        print (s)     
      
    def display_table(self,dealerscore,dealer_cards,playerscore,player_cards,player_funds,split = False,
                     player_score_2 = 0,player_cards_2 = []):
        '''takes in dealer score, player score, dealer cards, player cards, and player money'''
        '''prints all of these along with the pot'''
        print(f'DEALER SCORE:{dealerscore}')
        self.print_cards(dealer_cards)
        print('')
        print('')
        print(f'PLAYER SCORE:{playerscore}')
        self.print_cards(player_cards)
        print('')
        print(f'POT: ${self.pot}')
        if split == True:
            print('')
            print(f'PLAYER SCORE 2:{player_score_2}')
            self.print_cards(player_cards_2)
            print('')
            print(f'POT 2: ${self.pot2}')
        print('')
        print(f'PLAYER FUNDS: ${player_funds}')
    
class Player:
    '''a class for a player'''
    def __init__(self,name,money):
        '''initializes class with name, money, and card attributes'''
        self.name = name
        self.money = money
        self.all_cards = []
        
    def __str__(self):
        '''returns name when string is called'''
        return self.name
    
    def add_card(self,new_card):
        '''adds a card to their hand'''
        self.all_cards.append(new_card)
        
    def remove_card(self):
        '''removes a card from the players hand'''
        return self.all_cards.pop()
    
    def remove_all_cards(self):
        # NOT CURRENTLY IN USE
        '''removes all cards from the players hand'''
        for card in self.all_cards:
            self.all_cards.pop()
            
    def player_score(self):
        '''returns the score of a players hand'''
        '''automatically accounts for what value of ace will best benefit a players hand'''
        score = 0
        for card in self.all_cards:
            if card.visible == True:
                score += card.value
        
        for card in self.all_cards:
            if card.rank == 'Ace' and card.visible == True and \
              score <= 11:
                score += 10
        return score
            
    def bet(self,bet_amount):
        '''takes in a bet amount and verifys its a number'''
        '''makes sure its not over what the player currently has'''
        '''prints bet amount, removes it from player money, and returns it as an int'''
        while True:
            try:
                i = int(bet_amount)
                break
            except ValueError:
                i = 0
                break
                    
        if i not in range(1,self.money+1):
            print('Please choose a valid amount.')
            return 0
            
        else:
            print(f'{self.name} has bet {i} dollars.')
            self.money = self.money - int(i)
            return int(i)
    
    def receive(self,amount):
        '''takes an amount and adds it to players money'''
        self.money = self.money + amount
                
    def split(self,bet_amount):
        '''takes in original bet amount'''
        '''splits hand in two'''
        '''returns bet amount so it can be placed on new split hand'''
        self.split_1 = []
        self.split_2 = []
        self.split_1.append(self.all_cards[0])
        self.split_2.append(self.all_cards[1])
        return self.bet(bet_amount)
    
    def place_insurance(self,original_bet):
        # NOT CURRENTLY IN USE
        # NOT CURRENTLY IN USE
        # NOT CURRENTLY IN USE
        new_bet = 0
        while new_bet == 0:
            i = int(input(f'Please enter a bet up to 1/2 ${original_bet}: '))
            if i > (original_bet*.5):
                print('Bet entered is too high.')
                return
            else:
                new_bet == i
                break
        return new_bet

class Dealer:
    '''a class for the dealer'''
    def __init__(self):
        '''initializes dealer with attribute of cards held'''
        self.all_cards = []
    
    def add_card(self,new_card):
        '''adds a card to their hand'''
        self.all_cards.append(new_card)
        
    def remove_card(self):
        '''removes a card from their hand'''
        return self.all_cards.pop()
    
    def remove_all_cards(self):
        # NOT CURRENTLY IN USE
        '''removes all cards from their hand'''
        while len(self.all_cards) > 0:
            self.all_cards.pop()
            
    def dealer_score(self):
        '''returns the score of a dealer, automatically determines what value of Ace will go over 17 but not bust'''
        score = 0
        for card in self.all_cards:
            if card.visible == True:
                score += card.value
        for card in self.all_cards:
            if card.visible == True and card.rank == 'Ace' and \
              score + 10 >= 17 and score + 10 <= 21:
                score += 10
        return score

def get_yorno_input(prompt):
    '''universal function that makes sure an input is a Y or N, takes in prompt'''
    while True:
        try: i = (input(prompt).upper())
        except ValueError:
            print('Invalid input, try again.')
        
        if i in ['Y','N']:
            return i
        else:
            print('Invalid input, try again.')
            
def natural_push(player,dealer,table,bet):
    '''end game when a natural push occurs'''
    sleep(1.5)
    print('Natural Push!')
    print(f'Player receives back bet of ${bet}.')
    table.remove_pot(bet_amount)
    player.receive(bet_amount)
    table.display_table(dealer.dealer_score(),dealer.all_cards,
                            player.player_score(),player.all_cards,
                            player.money)
        
def player_busts(player,dealer,table,bet):
    '''end game when the player busts'''
    print('\n' * 100)
    table.remove_pot(bet)
    dealer.all_cards[-1].flip()
    table.display_table(dealer.dealer_score(),dealer.all_cards,
                            player.player_score(),player.all_cards,
                            player.money)
    print('')
    print('Score over 21! Player busts.')
    print(f'The player loses their bet of ${bet}')
    print(f'The dealers hidden card was a {str(dealer.all_cards[-1])}')
    
def game_over(player,dealer,table):
    '''asks player if they want to play again'''
    next_round = get_yorno_input(prompt = 'Would you like to play again? [Y/N] ')     
    if next_round == 'Y':
        # if yes, break hitting loop but keep game loop on
        while len(player.all_cards) > 0:
            table.add_discard(player.remove_card())
        while len(the_dealer.all_cards) > 0:
            table.add_discard(dealer.remove_card())
            
    return next_round

def player_natural(player,dealer,table,bet):
    '''ends game if a player gets a natural blackjack on the deal'''
    sleep(1.5)
    print('\n' * 100)
    table.display_table(dealer.dealer_score(),dealer.all_cards,
                            player.player_score(),player.all_cards,
                            player.money)
    reward = bet * 1.5
    reward = int(reward)
    print('')
    print('Player Natural!')
    print('')
    print(f'The player receives ${reward} on ${bet} bet!')
    table.remove_pot(bet)
    player.receive(reward)      
    print('')
    print('PLAYER FUNDS: $' + (str(player.money)))
    
def dealer_natural(player,dealer,table,bet):
    '''ends game if a dealer gets a natural blackjack on the deal'''
    sleep(1.5)
    print('Dealer Natural!')
    print(f'The player loses their bet of ${bet}!')
    table.remove_pot(bet_amount)
    print('PLAYER FUNDS: $' + (str(player.money)))

def double_down(player,dealer,deck,table,bet):
    '''asks the player if they would like to double down'''
    print('Would you like to double down?')
    doubledown = get_yorno_input(prompt = '(Double your bet and receive one last card)[Y/N] ')           
    if doubledown == 'Y':
        # deals a new card, calls the double down method which takes the bet amount, flips the card, adds it to
        # the players hand, adds a new pot to the table, table displays new hand and pot
        player.add_card(deck.deal_one())
        table.add_pot(bet)
        sleep(.5)
        table.display_table(dealer.dealer_score(),dealer.all_cards,
                                player.player_score(),player.all_cards,
                                player.money)
        return 'Y'    
    if doubledown == 'N':
        return 'N'
    
