#Hangman Game
#Players try to figure out an unknown word by guessing letters
#Each correct letter is added to dashed word
#Each wrong letter has their count -1

secret_word = "CAT" #sets the secret word: Please insert your or ask user to insert
guess_count = 3 
guessedLetters = "" #string to store guessed letters

while guess_count > 0:
    guess = input("\nPlease enter your guess letter: ").upper()
    if guess in secret_word:
        print(f'Congrats! There is one or more {guess} in secret word!')
    else:
        guess_count -= 1
        print(f"Sorry, there is no {guess} in secret word. Remaining attempts: {guess_count}")
        

    guessedLetters = guessedLetters + guess
    wrongGuessCount = 0

    for letter in secret_word:
        if letter in guessedLetters:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrongGuessCount += 1

    if wrongGuessCount == 0:
        print(f"\nCongratulations! You got the secret word: {secret_word}")
        break
else:
    print(f"\nYou ran out of guesses. The secret word was {secret_word}")
    
