import random


my_guesses = 3

while my_guesses > 0:
    random_number = random.randint(1, 10)
    guess = int(input("guess the number: "))

    if guess == random_number:
        print("you win")
    else:
        my_guesses -= 1
        print("you lose")