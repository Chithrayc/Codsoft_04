import random

continue_game = True

while continue_game:
    print(" *** Rock- Paper -Scissors Game ***")
    print (" \n ----- ALL THE BEST ----\n")
    
    user_choice = int(input("\n0 for Rock\n1 for Paper\n2 for Scissors \n Enter your choice: "))

    
    if user_choice < 0 or user_choice >= 3:
        print("Invalid choice, please choose 0, 1, or 2.")
        continue
    
   
    print(f" \n You chose {user_choice}:  ", end="")
    if user_choice == 0:
        print("Rock")
    elif user_choice == 1:
        print("Paper")
    elif user_choice == 2:
        print("Scissors")

   
    computer_choice = random.randint(0, 2)
    print(" Computer chose: ", end="")
    if computer_choice == 0:
        print("Rock")
    elif computer_choice == 1:
        print("Paper")
    elif computer_choice == 2:
        print("Scissors")

    
    if computer_choice == user_choice:
        print(" It's a draw.\n ")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print(" You win! \n ")
    else:
        print(" You lose.\n ")

    
    x = input("\n Continue the game (yes/no)? ").strip().lower()
    if x == "no":
        continue_game = False

print("Thank you for playing the Game !")
