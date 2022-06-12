import hangman_words
import hangman_art
import random


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
guessed = []

end_of_game = False
lives = 6


print(hangman_art.logo)

print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in guessed:
      print(f"You've already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            guessed.append(guess)
    if guess not in chosen_word:
        if guess in guessed:
          print(f"You've already guessed {guess}")
        else:
          guessed.append(guess)
          lives -= 1
          print(f"You guessed {guess}, that's not in the word. You lose a life.")
          if lives == 0:
              end_of_game = True
              print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
