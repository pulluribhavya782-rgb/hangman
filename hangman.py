import random

words = ["python", "computer", "programming", "developer", "keyboard"]

secret_word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")
print("The word has", len(secret_word), "letters.")
while attempts > 0:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guessed letters:", guessed_letters)
    print("Attempts left:", attempts)

    if "_" not in display_word:
        print("You won! 🎉")
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only ONE letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
    elif guess in secret_word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        guessed_letters.append(guess)
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("\nYou lost! 😢")
    print("The word was:", secret_word)