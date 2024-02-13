import random


def main():
    while True:
        try:
            number = int(input("Level: "))
            if number <= 0:
                raise ValueError
            rand_number = random.randint(1, number)
            guess_number(rand_number)
            break
        except ValueError:
            pass


def guess_number(n):
    while True:
        try:
            g = int(input("Guess: "))
            if g <= 0:
                raise ValueError
            if g == n:
                print("Just right!")
                break
            elif g < n:
                print("Too small!")
            elif g > n:
                print("Too large!")
        except ValueError:
            pass


main()
