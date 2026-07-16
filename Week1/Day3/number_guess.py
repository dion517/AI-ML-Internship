secret_number = 25

while True:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        break
    else:
        print("Incorrect guess. Try again.")