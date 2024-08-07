import random

from hangman_words import word_list
from hangman_art import stages, logo


def initialize_game():
    print(logo)
    chosen_word = random.choice(word_list)
    placeholder = "_" * len(chosen_word)
    print("Word to guess: " + placeholder)
    return chosen_word, placeholder


def update_display(chosen_word, correct_letters):
    return "".join([letter if letter in correct_letters else "_" for letter in chosen_word])


def play_hangman():
    lives = 6
    chosen_word, display = initialize_game()
    correct_letters = set()
    guessed_letters = set()
    game_over = False

    while not game_over:
        print(f"**************************** {lives}/6 LIVES LEFT ****************************")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print(f"You've already guessed {guess}")
            continue

        guessed_letters.add(guess)

        if guess in chosen_word:
            correct_letters.add(guess)
            display = update_display(chosen_word, correct_letters)
            print("Word to guess: " + display)
        else:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            print("Word to guess: " + display)
            print(stages[lives])

        if "_" not in display:
            game_over = True
            print("**************************** YOU WIN ****************************")
        elif lives == 0:
            game_over = True
            print(f"*********************** IT WAS {chosen_word}! YOU LOSE **********************")


if __name__ == "__main__":
    play_hangman()
