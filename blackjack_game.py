from blackjack_classes_funcs import Card, Deck, Table, Player, Dealer
from blackjack_classes_funcs import get_yorno_input, natural_push, player_busts 
from blackjack_classes_funcs import game_over, player_natural, dealer_natural, double_down
from time import sleep
import random

    # Sets up the player with a name and starting amount of money
    # Sets up a dealer
    # Creates a deck
    # Creates a table
    # Shuffles the deck
    # Resets the player and dealer score to zero, along with blackjack indicators to false

print('Welcome to Blackjack!')
name = input('Please enter your name: ')
print(f'Welcome {name}, you will start with $1000')
the_player = Player(name,1000)
the_dealer = Dealer()
num_decks = 5
game_deck = Deck()
i = 0
while i < num_decks:
    new_deck = Deck()
    game_deck.combine(new_deck)
    i += 1
the_table = Table()
game_deck.shuffle()

game_on = True
while game_on:

    ask_tohit = True
    dealer_turn = False
    dealer_hits = False
    player_blackjack = False
    dealer_blackjack = False
    settled = False
    will_hit = ''
    bet_amount = 0
        # also resets will_hit variable and bet amount variable
    while bet_amount == 0:
            # this loop takes in a bet amount and adds it to the player,
            # will return an error if its not valid
        i = input(f'{the_player}, please enter a bet amount: $')
        bet_amount = the_player.bet(i)
        
    the_table.add_pot(bet_amount)
        # adds the bet amount to the pot
    
    for x in range(0,4):
        # this loop deals out 4 cards, printing for each new card, and flips the last card that is given to the dealer
        # also adds togther values of card totals
        if x == 0 or x == 2:
            the_player.add_card(game_deck.deal_one())
            the_table.display_table(the_dealer.dealer_score(),the_dealer.all_cards,
                                    the_player.player_score(),the_player.all_cards,
                                    the_player.money)
            sleep(.7)
            print('\n' * 100)
        elif x == 1:
            new_card = game_deck.deal_one()
            the_dealer.add_card(new_card)
            the_table.display_table(the_dealer.dealer_score(),the_dealer.all_cards,
                                    the_player.player_score(),the_player.all_cards,
                                    the_player.money)
            sleep(.7)
            print('\n' * 100)
        elif x == 3:
            new_card = game_deck.deal_one()
            new_card.flip()
            the_dealer.add_card(new_card)
            the_table.display_table(the_dealer.dealer_score(),the_dealer.all_cards,
                                    the_player.player_score(),the_player.all_cards,
                                    the_player.money)
            
    if the_player.player_score() == 21:
        # checks if the player has blackjack
        player_blackjack = True
        
    if the_dealer.all_cards[0].value == 10 or 11:
        # if the dealers first card is a face or an ace, checks the face down card and adds it to the score
        the_dealer.all_cards[-1].flip()
        if the_dealer.dealer_score() == 21:
            # if this gives the dealer a blackjack, set to true
            dealer_blackjack = True
        else:
            # if its not a blackjack, resubstracts the flipped cards value
            # so only the visible cards value is in the printed dealer score
            the_dealer.all_cards[-1].flip()
    if dealer_blackjack == True:
        # flips card to show full hand
        sleep(1.5)
        print('\n' * 100)
        the_table.display_table(the_dealer.dealer_score(),the_dealer.all_cards,
                                the_player.player_score(),the_player.all_cards,
                                the_player.money)
        
    if dealer_blackjack == True and player_blackjack == True:
        # if its a tie, prints this, returns players bet amount, removes it from the pot...
        # removes the cards from both the players and the dealers hands
        # resets score
        # prints cleared table
        # asks if player wants another round
        natural_push(the_player,the_dealer,the_table,bet_amount)
        settled = True
        choice = game_over(the_player,the_dealer,the_table)
        if choice == 'N':
            game_on = False
            break     
        if choice == 'Y':
            ask_tohit = False
    
    if player_blackjack == True and dealer_blackjack == False:
        # if player wins on first go, prints this, calculates the rewards as 1.5X the bet, returns the reward
        # to the player, empties the pot, removes cards from both players and dealers hands
        # resets score to zero, prints cleared table, and asks if player wants another round
        player_natural(the_player,the_dealer,the_table,bet_amount)
        settled = True
        choice = game_over(the_player,the_dealer,the_table)
        if choice == 'N':
            game_on = False
            break     
        if choice == 'Y':
            ask_tohit = False
        
    if dealer_blackjack == True and player_blackjack == False:
        # if dealer wins, empties the pot, prints this, empties both players and dealers hands
        # resets scores, prints cleared table
        # asks if player wants another round
        dealer_natural(the_player,the_dealer,the_table,bet_amount)
        settled = True
        choice = game_over(the_player,the_dealer,the_table)
        if choice == 'N':
            game_on = False
            break     
        if choice == 'Y':
            ask_tohit = False
                       
    if the_player.player_score() in(9,10,11):
        # checks if a players total score is within 9 - 11, if so asks if they want to double down
        choice = double_down(the_player,the_dealer,game_deck,the_table,bet_amount)
        if choice == 'Y':
            ask_tohit = False
            dealer_turn = True

    while ask_tohit == True:
        # if game isn;t already over, starts a loop for asking to hit
        will_hit = get_yorno_input(prompt = f'{str(the_player)}, would you like to hit? [Y/N] ')
        if will_hit == 'N':
            # breaks loop and goes on to dealers turn
            print('...')
            print('Player Stands')
            sleep(1.5)
            dealer_turn = True
            break
        if will_hit == 'Y':
            # adds a new card to the players hand, adds value to score, prints new table with this card and score
            print('')
            print('Player Hits')
            print('...')
            sleep(1.5)
            new_card = game_deck.deal_one()
            the_player.add_card(new_card)
            print('\n' * 100)
            the_table.display_table(the_dealer.dealer_score(),the_dealer.all_cards,
                                    the_player.player_score(),the_player.all_cards,
                                    the_player.money)
            print('...')
            sleep(1.5)
            
            if the_player.player_score() > 21:
                player_busts(the_player,the_dealer,the_table,bet_amount)
                choice = game_over(the_player,the_dealer,the_table)
                settled = True
                if choice == 'N':
                    game_on = False
                    ask_tohit = False
                if choice == "Y":
                    ask_tohit = False
                    
            if the_player.player_score() == 21:
                # if player hits 21, goes to dealers turn
                ask_tohit = False
                dealer_turn = True
                break
                
    while dealer_turn == True:
        the_dealer.all_cards[1].flip()
        print('')
        print('Dealer flips.')
        print('...')
        sleep(1.5)
        print('\n' * 100)
        if the_dealer.dealer_score() >= 17:
            the_table.display_table(the_dealer.dealer_score(),the_dealer.all_cards,
                                    the_player.player_score(),the_player.all_cards,
                                    the_player.money)
            sleep(1.5)
            print('')
            print('Dealer stands, go to settle.')
            dealer_turn = False
            break
        if the_dealer.dealer_score() <= 16:
            dealer_hits = True
            print('')
            print('Dealer hits')
            the_table.display_table(the_dealer.dealer_score(),the_dealer.all_cards,
                                    the_player.player_score(),the_player.all_cards,
                                    the_player.money)
            sleep(1.5)
            print('\n' * 100)
            while dealer_hits == True:
                print('Dealer hits')
                print('')
                sleep(1)
                new_card = game_deck.deal_one()
                the_dealer.add_card(new_card)
                the_table.display_table(the_dealer.dealer_score(),the_dealer.all_cards,
                                        the_player.player_score(),the_player.all_cards,
                                        the_player.money)
                if the_dealer.dealer_score() > 21:
                    print('')
                    print('Dealer busts!')
                    reward = bet_amount * 1.5
                    reward = int(reward)
                    print('...')
                    sleep(1)
                    print(f'The player receives ${reward} on ${bet_amount} bet!')
                    the_table.remove_pot(bet_amount)
                    the_player.receive(reward)
                    settled = True
                    
                    print('PLAYER FUNDS: $' + (str(the_player.money)))
                    
                    choice = game_over(the_player,the_dealer,the_table)
                    
                    if choice == 'N':
                        game_on = False
                        dealer_turn = False
                        break 
                    if choice == 'Y':
                        dealer_turn = False
                        break
            
                if the_dealer.dealer_score() >= 17:
                    print('Dealer stands! Go to settle.')
                    dealer_turn = False
                    break
                else:
                    sleep(1.5)
                    print('\n' * 100)
    
    while settled == False:
        
        for card in the_player.all_cards:
            if card.visible == False:
                print('Flipping double down card.')
                print('...')
                card.flip()
                sleep(1.5)
                the_table.display_table(the_dealer.dealer_score(),the_dealer.all_cards,
                                       the_player.player_score(),the_player.all_cards,
                                       the_player.money)
            
        if the_dealer.dealer_score() > the_player.player_score():
            sleep(1.5)
            print('Dealer wins!')
            print(f'Player loses bet amount of ${bet_amount}')
            the_table.remove_pot(bet_amount)
            
        if the_dealer.dealer_score() < the_player.player_score():
            sleep(1.5)
            print('Player wins!')
            reward = bet_amount * 1.5
            reward = int(reward)
            print(f'The player receives ${reward} on ${bet_amount} bet!')
            the_table.remove_pot(bet_amount)
            the_player.receive(reward)
            
        elif the_dealer.dealer_score() == the_player.player_score():
            sleep(1.5)
            print('Stand off!')
            print(f'Player receives back bet of ${bet_amount}.')
            the_table.remove_pot(bet_amount)
            the_player.receive(bet_amount)
            
        sleep(1.5)
        print('')
        print('PLAYER FUNDS: $' + (str(the_player.money)))
        choice = game_over(the_player,the_dealer,the_table)
        if choice == 'N':
            # if no, turn of the game and hitting loop and break it
            game_on = False
            settled = True
            break
                    
        if choice == 'Y':
            settled = True
            break   
