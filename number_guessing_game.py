import random

def main():
    while True:
        comp_choice = random.randint(1, 10)
        attempts = 3

        while attempts > 0:
            try:
                user_guess = int(input("\nGuess a number between 1 and 10: "))
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            else:
                if user_guess == comp_choice:
                    print("You guessed right!")
                    break
                else:
                    attempts -= 1
                    print(f"You guessed wrong! You have {attempts} attempt(s) left")

        if attempts == 0:
            print(f"\nYou have ran out of attempts, the number was {comp_choice}")

        while True:
            play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()

            if play_again in ['yes', 'y']:
                break
            elif play_again in ['no', 'n']:
                print("Thank you for playing!")
                return
            else:
                print("Invalid input. Please try again.")


main()