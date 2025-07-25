import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0

    print("I have chosen a number between 1 and 100.")
    print("Can you guess it? Let's try!")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < number:
                print("Try a higher number.")
            elif guess > number:
                print("Try a lower number.")
            else:
                print(f"Awesome! You guessed it right in {attempts} tries. Congrats!")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_number()
