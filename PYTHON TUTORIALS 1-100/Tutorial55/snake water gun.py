import random

def user_choice():
    choice = input("Enter your choice (snake/water/gun): ").lower()
    while choice not in ["snake", "water", "gun"]:
        print("Invalid Syntax..")
        choice = input("Please pick Snake/Water/Gun: ").lower()
    return choice

def comp_choice():
    choices = ["snake", "water", "gun"]
    return random.choice(choices)

# user_choice()
# comp_choice()
def winner(user, computer):
    if user == computer:
        return "It's a tie"
    elif user == "snake":
        return "You win!" if computer == "water" else "Computer wins!"
    elif user == "water":
        return "You win!" if computer == "gun" else "Computer wins!"
    elif user == "gun":
        return "You win!" if computer == "snake" else "Computer wins!"

def snake_water_gun_game():
    print("Welcome to snake water and gun game.")
    
    user = user_choice()
    computer = comp_choice()
    
    print(f"Your choice: {user}")
    print(f"Computer choice: {computer}")
    
    result = winner(user, computer)
    print(result)

if __name__ == "__main__":
    snake_water_gun_game()
    




    
    
    
    