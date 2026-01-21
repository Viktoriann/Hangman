import random
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

chosen_word = random.choice(word_list)
# print(chosen_word)

placeholder = ""

for position in range(len(chosen_word)):
    placeholder += "_"

print(placeholder)

correct_letters = []

game_over = False

lives = 6

while not game_over:

    print(f"**************************** {lives}/6 LIVES LEFT ****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed '{guess}'.")

    display = ""

    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        elif letter == guess:
            display += letter
            correct_letters.append(letter)
        else:
            display += "_"


    if guess not in chosen_word:
        print(f"'{guess}' is not in the word. You lose a life.")
        lives -= 1

    print(display)

    if "_" not in display:
        game_over = True
        print(f"**************************** YOU WIN! ****************************")
    if lives == 0:
        game_over = True
        print(f"**************************** IT WAS {chosen_word}! YOU LOSE! ****************************")

    print(stages[lives])


