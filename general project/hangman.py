import random
import hangman_logo
import hangman_word

print(hangman_logo.logo)

end_of_game = False
chosen_word = random.choice(hangman_word.word_list)
word_length = len(chosen_word)

lives = 6

print(f"Psst, the solution is {chosen_word}")

display =[]

for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter:\n").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position:{position}\nCurrent letter: {letter}\nGuessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    #print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(hangman_logo.stages[lives])

