import random

money = 100

#This is the code for the coin flip game

def coin_flip(): 
    global money
    print("Welcome to the coin flip game!")
    print("You have £" + str(money) + " in your wallet.")
    bet = bet_valid("How much would you like to bet? £")
    flip = random.randint(1,2)
    guess = input("Heads or tails? ")
    guess = guess.lower()
    if guess == "heads" and flip == 1:
        print("The coin landed on heads!")
        winnings = bet*2
        money += winnings
        print("Congratulations, you won! Your winnings are £" + str(winnings))
        play_again_flip()
    elif guess == "tails" and flip == 2:
        print("The coin landed on tails!")
        winnings = bet*2
        money += winnings
        print("Congratulations, you won! Your winnings are £" + str(winnings))
        play_again_flip()
    elif guess =="heads" and flip == 2:
        print("The coin landed on heads!")
        money += (bet*-1)
        print("Sorry, you lost. You have lost £" + str(bet))
        play_again_flip()
    else:
        print("The coin landed on tails!")
        print("Sorry, you lost. You have lost £" + str(bet))
        money += (bet*-1)
        play_again_flip()
        
#This is the code for Cho-Han

def cho_han():
    global money
    print("Welcome to Cho-Han! This game involves betting whether the sum of two dice rolls is even, or odd.")
    print("You have £" + str(money) + " in your wallet.")
    bet = bet_valid("How much would you like to bet? £")
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dicesum = dice1+dice2
    guess = input("Odd or even? ")
    guess = guess.lower()
    print("The dice were rolled. They were " + str(dice1) + " and " + str(dice2) + ".")
    if guess == "odd" and (dicesum)%2==1:
        print("The result is odd.")
        winnings = bet*2
        money += winnings
        print("Congratulations, you won! Your winnings are £" + str(winnings))
        play_again_cho_han()
    elif guess == "even" and (dicesum)%2 == 0:
        print("The result is even.")
        winnings = bet*2
        money += winnings
        print("Congratulations, you won! Your winnings are £" + str(winnings))
        play_again_cho_han()
    elif guess == "odd" and (dicesum)%2==0:
        print("The result is even.")
        money += (bet*-1)
        print("Sorry, you lost. You have lost £" + str(bet))
        play_again_cho_han()

    else:
        print("The result is odd.")
        money += (bet*-1)
        print("Sorry, you lost. You have lost £" + str(bet))
        play_again_cho_han()


def card_draw():
    global money
    print("Welcome to Two Card Draw! This game involves you and the dealer drawing a card each from a pack of cards. The highest card wins. Ace is high. If you both draw the same card, your bet is returned.")
    print("You have £" + str(money) + " in your wallet.")
    bet = bet_valid("How much would you like to bet? £")
    deck1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    deck2 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    card1index = random.choice(range(len(deck1)))
    card2index = random.choice(range(len(deck2)))
    card1 = deck1[card1index]
    card2 = deck2[card2index]
    print("The dealer drew " + card1 + ". You drew " + card2 + ".")
    if card2index > card1index:
        print("You have the higher card.")
        winnings = bet*2
        money += winnings
        print("Congratulations, you won! Your winnings are £" + str(winnings))
        play_again_cards()
    elif card1index > card2index:
        print("The dealer has the higher card.")
        winnings = bet*-1
        money += winnings
        print("Sorry, you lost. You have lost £" + str(bet))
        play_again_cards()
    else:
        print("It's a draw!")
        play_again_cards()

def roulette():
    global money
    print("Welcome to the roulette table! This game involves betting on the outcome of a spin of a roulette wheel. You can bet on odd, even, red, black or a specific number, from 0 to 35.")
    bet = bet_valid("How much would you like to bet? £")
    guess = input("What would you like to gamble? You can enter red, black, odd, even, or a specific number. ")
    result = random.randint(0,35)
    print("The wheel spins, and the ball lands on " + str(result))
    if guess == result:
        winnnings = bet*35
        money += winnings
        print("Congratulations! You hit the jackpot! Your winnings are £" + str(winnings))
        play_again_roulette()
    elif result%2 == 0 and guess == "even":
        winnings = bet*2
        money += winnings
        print("Congratulations! You win! Your winnings are £" + str(winnings))
        play_again_roulette()
    elif result%2 == 1 and guess == "odd":
        winnings = bet*2
        money += winnings
        print("Congratulations! You win! Your winnings are £" + str(winnings))
        play_again_roulette()
    else:
        money = money-bet
        print("Commiserations, you have lost.")
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
            choice = None
        if choice == 2:
            cho_han()
            choice = None
        if choice == 3:
            card_draw()
            choice = None
        if choice == 4:
            roulette()
            choice = None
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

#These functions handle input validation

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

#Write your game of chance functions here



#Call your game of chance functions here
