import random

def main():
    random.seed()
    number = random.randint(1, 100)
    guess = 0

    while guess != number:
        guess = int(input("Enter Guess (1-100): "))
        if guess > number:
            print("Guess lower!")
        elif guess < number:
            print("Guess higher!")
        else:
            print("You won!")

if __name__ == "__main__":
    main()
