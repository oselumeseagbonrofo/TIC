import random

computer_score = 0
player_score = 0
moves = ("rock", "paper", "scissors")

player_name = input("What is your name? ")
print(player_name + " Welcome to Oselumese's Rock Paper Scissors game")


# determines if player made a valid input
def determine_valid_player_input():
    player = input("Please input either rock, paper or scissors: ").lower()

    if player in moves:
        return player

    else:
        print("Invalid input")
        # determine_valid_player_input()
        return player


# displays result if computer is the winner
def computer_result_display():
    result = "Player: " + player_input + "\nComputer: " + computer_input + "\nPlayer loses" + "\nPlayer-" + str(
        player_score) + " " + str(computer_score) + "-Computer"
    print(result)


# displays result if the player is the winner
def player_result_display():
    result = "Player: " + player_input + "\nComputer: " + computer_input + "\nPlayer wins" + "\nPlayer-" + str(
        player_score) + " " + str(computer_score) + "-Computer"
    print(result)


# displays result if it is a tie
def tie_result_display():
    result = "Player: " + player_input + "\nComputer: " + computer_input + "\nIt is a tie" + "\nPlayer-" + str(
        player_score) + " " + str(computer_score) + "-Computer"
    print(result)

# determines if player wants to continue the game
def another_round():
    new_round = input("Do you wish to continue this game y/n ").lower()
    if new_round == "y":
        pass
    else:
        exit("Thank you for playing " + player_name)


#determines the winner of a round
while True:
    computer_input = random.choice(moves)
    player_input = determine_valid_player_input()
    if player_input == "rock" and computer_input == "scissors":
        player_score += 1
        player_result_display()
        another_round()
    elif player_input == "scissors" and computer_input == "rock":
        computer_score += 1
        computer_result_display()
        another_round()
    elif player_input == "rock" and computer_input == "paper":
        computer_score += 1
        computer_result_display()
        another_round()
    elif player_input == "paper" and computer_input == "rock":
        player_score += 1
        player_result_display()
        another_round()
    elif player_input == "scissors" and computer_input == "paper":
        player_score += 1
        player_result_display()
        another_round()
    elif player_input == "paper" and computer_input == "scissors":
        computer_score += 1
        computer_result_display()
        another_round()
    elif player_input == computer_input:
        tie_result_display()
        another_round()
    else:
        pass
