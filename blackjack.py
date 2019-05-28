"""
This is a blackjack/twenty-one game. The objective of the game is to draw cards
and obtain the highest total not exceeding 21.
"""
import random

def pick_a_card():
    """
    This function randomly picks a number between 2 and 10
    """
    card = random.randint(1, 10)
    return card

def total_value(value1, value2):
    """
    This function returns the sum of 2 numbers
    """
    return value1+value2

def check_valid_character(valid_option_1, valid_option_2, value_entered):
    """
    This function will check if the input for y/n and h/s questions are valid
    """
    if value_entered.isalpha() == 1:
        valid_option_1 = valid_option_1.upper()
        valid_option_2 = valid_option_2.upper()
        value_entered = value_entered.upper()
        if value_entered in (valid_option_1, valid_option_2):
        #if value_entered == valid_option_1 or value_entered == valid_option_2:
            result = 1
        else:
            result = 0
    else:
        result = 0
    return result

def user_choice(option_1, option_2, choice):
    """
    This function validates the user input, and asks the user to enter a valid
    value
    """
    input_string = {'y': ["Do you want to start a new game? (y/n): "]}
    input_string['h'] = ["Hit or Stand? (h/s): "]
    valid = check_valid_character(option_1, option_2, choice)
    while valid != 1:
    #    print(input_string[option_1][0])
        print("You have entered an invalid value.\n")
        choice = input(input_string[option_1][0])
        valid = check_valid_character(option_1, option_2, choice)
    return choice

def draw_line():
    """
    This function draws a line
    """
    print(f"{'-':-^60}")

def hit(total):
    """
    This function performs a blackjack hit.  It picks a card, and determines
    the players new total.
    """
    card = pick_a_card()
    total = total_value(total, card)
    return card, total

def determine_winner(dealer_total, player_total):
    """
    This function determines who the winner of the blackjack game is based on
    who draws a card closest to 21
    """
    if dealer_total > 21:
        result = "The dealer bust.  The You WIN!!!\n"
    elif dealer_total == 21 and player_total == 21:
        result = "The dealers and your totals are equal.  The dealer wins.\n"
    elif dealer_total == player_total:
        result = "Dealer total is the same as yours.  The Dealer wins.\n"
    elif player_total <= dealer_total <= 21:
        result = "The dealers total is greater than yours. The Dealer wins.\n"
    elif dealer_total < player_total <= 21:
        result = "Your total cards are greater than the Dealers.  You Win!!!!.\n"
    return result

def dealers_play(card, total):
    """
    This function represents the dealers turn in the game.
    """
    print(f'\nThe dealers hidden card was a {card}.\n')
    print(f'The dealers total was {total}.\n')
    while total < 17:
        card, total = hit(total)
        print(f'The dealer chooses to HIT!')
        print(f'The dealer draws a {card}.')
        print(f'The dealers total is {total}.\n')
    return total

def deal_cards():
    """
    This function randomly picks 4 cards to begin the game of blackjack.
    2 cards for the player and 2 cards for the dealer
    """
    card_1 = pick_a_card()
    card_2 = pick_a_card()
    card_3 = pick_a_card()
    card_4 = pick_a_card()
    return(card_1, card_2, card_3, card_4)

if __name__ == '__main__':
    CONTINUE_PLAYING = 'y'
    print("\nWelcome to Blackjack\n")
    while CONTINUE_PLAYING == 'y':
        CONTINUE_PLAYING = input("Do you want to start a new game? (y/n): ")
        CONTINUE_PLAYING = user_choice('y', 'n', CONTINUE_PLAYING)

        if CONTINUE_PLAYING == 'y':
            PLAYER_CARD_1, PLAYER_CARD_2, DEALER_CARD_1, DEALER_CARD_2 = deal_cards()
            PLAYER_TOTAL = total_value(PLAYER_CARD_1, PLAYER_CARD_2)
            DEALER_TOTAL = total_value(DEALER_CARD_1, DEALER_CARD_2)
            print(f'\nYou are dealt a {PLAYER_CARD_1} and a {PLAYER_CARD_2}.')
            print(f'Your total is {PLAYER_TOTAL}.\n')
            print(f'The dealer dealt a {DEALER_CARD_1} and a hidden card.\n')

            HIT_OR_STAND = input("Hit or Stand? (h/s): ")
            HIT_OR_STAND = user_choice('h', 's', HIT_OR_STAND)

            if HIT_OR_STAND == 'h':
                while HIT_OR_STAND == 'h':
                    PLAYER_CARD, PLAYER_TOTAL = hit(PLAYER_TOTAL)
                    print(f'\nHit! You draw a {PLAYER_CARD}.')
                    print(f'Your total is {PLAYER_TOTAL}.\n\n')
                    if PLAYER_TOTAL > 21:
                        break
                    else:
                        HIT_OR_STAND = input("Hit or Stand? (h/s): ")
                        HIT_OR_STAND = user_choice('h', 's', HIT_OR_STAND)

                if PLAYER_TOTAL > 21:
                    print("You bust. The Dealer wins\n")
                    draw_line()
                    continue

                else:
                    DEALER_TOTAL = dealers_play(DEALER_CARD_2, DEALER_TOTAL)

            elif HIT_OR_STAND == 's':
                if PLAYER_TOTAL <= 21:
                    DEALER_TOTAL = dealers_play(DEALER_CARD_2, DEALER_TOTAL)

            WINNER = determine_winner(DEALER_TOTAL, PLAYER_TOTAL)
            print(WINNER)
            draw_line()
        else:
            print("\nThanks for Playing. See you in the next game.")
            break






#The possible card values range from 1 to 10 and, unlike a real deck, the
# probability of drawing a card is equal
#The game begins by dealing two visible cards to the player (face up), and two
#cards to the dealer. However, in the case of the dealer, one card is visible
#to other players while the other is hidden.
#The player decides whether to "hit" (draw another card), or "stand" which ends
#their turn.
#The player may hit any number of times. Should the total of the cards exceed
#21, the player "busts" and loses the game to the dealer.


#hit draws a new card
#stand ends the players tur
#randomize players first 2 draws(range from 1 to 10)
#randomize dealers first 2 draws (range from 1 to 10).  The second card remins
#hidden until the player stands or reaches 21
#At this point the dealer revels the hidden card
#The dealer must hit if the total is 16 or less, and must stand if the value is
#17 or more
#The dealer wins all ties (i.e. if both the dealer and the player reach 21, the
#dealer wins)
#The program indicates who the winner is and asks to play again

#if the total exceeds 21 the player busts and loses the game
