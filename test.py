import random

def play_number_guessing_game(number_of_attempts):
    random_number = random.randint(1, 10)
    attempts = 0

    while attempts < number_of_attempts:
        try:
            number = int(input("Enter your guess (1-10): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        attempts += 1

        if random_number == number:
            print("Congratulations! You guessed the number correctly.")
            break
        elif number > random_number:
            print("Too high!")
        else:
            print("Too low!")

    if attempts == number_of_attempts:
        print("Game over! You have reached the maximum number of attempts.")
        print(f"The secret number was: {random_number}")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_number_guessing_game(number_of_attempts)

number_of_attempts = int(input("Number of attempts: "))
play_number_guessing_game(number_of_attempts)
