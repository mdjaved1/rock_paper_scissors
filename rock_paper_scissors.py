import random

user_wins = 0
computer_wins = 0 
options = ["rock", "paper", 'scissors']

while True:
    user_input = input("type Rock/Paper/Scissors or Q to quit. ").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    #0 is rock, 1 is paper, 2 is scissors    
    computer_pick = options[random_number]
    print ("computer picked ", computer_pick + ".")
    if user_input == "paper" and computer_pick == "rock":
        user_wins += 1
        print("you won!")
    elif user_input == "scissors" and computer_pick == "paper":
        print("you won!")
        user_wins += 1
    elif user_input == "rock" and computer_pick == "scissors":
        print("you won!")
        user_wins += 1
    else:
        print("You lost !")
    computer_wins += 1
        

print("you won", user_wins, "times.")
print("computer won",computer_wins, "times.")
print("Good bye! ")