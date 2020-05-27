import random

money = 100

#This is the code for the coin flip game

def coin_flip(): 
    global money
    print("Welcome to the coin flip game!")
    print("You have £" + str(money) + " in your wallet.")
    bet = bet_valid("How much would you like to bet? £")
    flip = random.randint(1,2)

    def successful_flip(result):
        global money
        print("The coin landed on " + str(result))
        money+= bet*2
        print("Congratulations, you won! Your winnings are £" + str(bet*2) +".")
        play_again_flip()

    def unsuccessful_flip(result):
        global money
        print("The coin landed on " + str(result))
        money += bet*-1
        print("Sorry, you lost. You have lost £" + str(bet) + ".")
        play_again_flip()

    while True:
        try:
         guess = int(input("""Which way will the coin land?

            1. Heads
            2. Tails

            :"""))
        except ValueError:
            print("Sorry, I don't understand that. Please use a number to pick either heads or tails.")
            continue
        if guess == 1 and flip == 1:
            successful_flip("heads.")
        elif guess == 2 and flip == 2:
            successful_flip("tails.")
        elif guess == 1 and flip == 2:
            unsuccessful_flip("tails.")
        elif guess ==2 and flip == 1: 
            unsuccessful_flip("heads.")
        else:
            print("Please pick either heads or tails!")
            continue

        
#This is the code for Cho-Han

def cho_han():
    global money
    print("""Welcome to Cho-Han! 
    This game involves betting whether the sum of two dice rolls is even, or odd.""")
    print("You have £" + str(money) + " in your wallet.")
    bet = bet_valid("How much would you like to bet? £")
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dicesum = dice1+dice2

    def winning_roll(result):
        global money
        print("The dice were rolled. They were " + str(dice1) + " and " + str(dice2) + ".")
        print("The result is " + result)
        money += bet*2
        print("Congratulations, you won! Your winnings are £" + str(bet*2))
        play_again_cho_han()

    def losing_roll(result):
        global money
        print("The dice were rolled. They were " + str(dice1) + " and " + str(dice2) + ".")
        print("The result is " + result)
        money += (bet*-1)
        print("Sorry, you lost. You have lost £" + str(bet))
        play_again_cho_han()

    while True:
        try:
            guess = int(input("""Odd or even? 

                1. Odd
                2. Even

                :"""))
        except ValueError:
            print("Sorry, I don't understand that. Please use a number to pick either odd or even.")
            continue
        if guess == 1 and (dicesum)%2==1:
            winning_roll("odd.")
        elif guess == 2 and (dicesum)%2 == 0:
            winning_roll("even.")
        elif guess == 1 and (dicesum)%2==0:
            losing_roll("even.")
        elif guess == 2 and (dicesum)%2==1:
            losing_roll("odd.")
        else:
            print("Please pick either odd or even.")
            continue

# This is the code for two card draw

def card_draw():
    global money
    print("""Welcome to Two Card Draw! 
        This game involves you and the dealer drawing a card each from a pack of cards. The highest card wins. Ace is high. If you both draw the same card, your bet is returned.""")
    print("You have £" + str(money) + " in your wallet.")
    bet = bet_valid("How much would you like to bet? £")
    deck = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    card1index = random.choice(range(len(deck)))
    card2index = random.choice(range(len(deck)))
    card1 = deck[card1index]
    card2 = deck[card2index]
    print("The dealer drew " + card1 + ". You drew " + card2 + ".")
    if card2index > card1index:
        print("You have the higher card.")
        money += bet*2
        print("Congratulations, you won! Your winnings are £" + str(bet))
        play_again_cards()
    elif card1index > card2index:
        print("The dealer has the higher card.")
        money += bet*-1
        print("Sorry, you lost. You have lost £" + str(bet))
        play_again_cards()
    else:
        print("It's a draw!")
        play_again_cards()

# This is the code for roulette

def roulette():
    global money
    print("Welcome to the roulette table! This game involves betting on the outcome of a spin of a roulette wheel. You can bet on odd, even, red, black or a specific number, from 0 to 35.")
    print("You have £" + str(money) + " in your wallet.")
    bet = bet_valid("How much would you like to bet? £")
    guess = input("What would you like to gamble? You can enter red, black, odd, even, or a specific number. ")
    result = random.randint(0,36)

    def colour():
        if result == 0:
            colour = "Green "
            return colour
        elif result%2 == 0:
            colour = "Black "
            return colour
        elif result%2 == 1:
            colour = "Red "
            return colour

    def winning_bet():
        global money
        money+=bet*2
        print ("Congratulations, you win! Your winnings are £" + str(bet))
        play_again_roulette()


    print("The wheel spins, and the ball lands on " + str(colour()) + str(result))
    if guess == result:
        money += bet*35
        print("Congratulations! You hit the jackpot! Your winnings are £" + str(bet*35))
        play_again_roulette()
    elif result%2 == 0 and guess.lower() == "even":
        winning_bet()
    elif result%2 == 1 and guess.lower() == "odd":
        winning_bet()
    elif result%2 == 0 and guess.lower() == "black":
        winning_bet()
    elif result%2 == 1 and guess.lower() == "red":
        winning_bet()
    else:
        money = money-bet
        print("Unfortunately you have lost £" + str(bet))
        play_again_roulette()



#This code handles the game selection by the player
        
def game_choice():
    while True:
        try:
            choice = int(input("""Please pick a game:

        1. Coin Flip
        2. Cho-Han
        3. Two Card Draw
        4. Roulette

        : """))
        except ValueError:
            print("Sorry, I don't understand that.")
            continue

        if choice == 1:
            coin_flip()
        if choice == 2:
            cho_han()
        if choice == 3:
            card_draw()
        if choice == 4:
            roulette()
        else:
            print("I'm sorry, I don't know that game")

def play_again_flip():
    print("You now have £" + str(money) + " in your wallet")
    playagain = input("Would you like to play again? (Y/N): ")
    if playagain == "Y":
        coin_flip()
    else:
        game_choice()
        
def play_again_cho_han():
    print ("You now have £" + str(money) + " in your wallet")
    playagaincho = input("Would you like to play again? (Y/N): ")
    if playagaincho == "Y":
        cho_han()
    else:
        game_choice()

def play_again_cards():
    print ("You now have £" + str(money) + " in your wallet.")
    playagaincards = input("Would you like to play again? (Y/N): ")
    if playagaincards == "Y":
        card_draw()
    else:
        game_choice()

def play_again_roulette():
    print("You now have £" + str(money) + " in your wallet.")
    playagainroulette = input("Would you like to play again? (Y/N): ")
    if playagainroulette == "Y":
        roulette()
    else:
        game_choice()

#This function handles betting input validation

def bet_valid(prompt):
    global money 
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I don't understand that.")
            continue

        if value < 0:
            print("Sorry, your bet cannot be negative")
            continue
        if value > money:
            print("Sorry, you cannot bet more than you have in your wallet!")
        else:
            break
    return value

    
Welcome = print(""""Welcome to Josh's Casino Game!

You enter the casino with £""" + str(money) + """ in your pocket. There are a number of games available to play.""")

Welcome

game_choice()
