import random

secret_num = random.randint(1, 10)

def menu():
    print("1. Play the number guessing game")
    print("2. Exit")

def game():
    guess = int(input("Enter a number : "))
    try:
        if guess < secret_num :
            print("Too low try again!")
        elif guess > secret_num :
            print("Too high, try again!")
        else:
            print(f"Congratulations you won! secret number is '{guess}'")
    except ValueError:
        print("Invalid Number")

while True:
    menu()
    choice = int(input("Choose an option : "))

    while choice == 1:
        game()
    if choice == 2:
        print("Good bye")
        break
    else:
        print("Invalid choice")