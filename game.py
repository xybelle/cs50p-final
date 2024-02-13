import random


def main():
    while True:
        try:
            number = int(input("Level: "))
            if number <= 0:
                raise ValueError
            guess_number(number)
            break
        except ValueError:
            pass


def guess_number(number):
    while True:
        try:
            n = random.randint(1, number)
            g = int(input("Guess: "))
            if g == n:
                print("Just right!")
                break
            elif g < n:
                print("Too small!")
                break
            elif g > n:
                print("Too large!")
                break
            else:
                raise ValueError
        except ValueError:
            pass


main()
