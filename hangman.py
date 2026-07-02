#The import random is use to choose a random words from the list of words
import random
# List of words {it is used to stores the all possible words for the game}
words = ["python", "apple", "coding", "computer", "program","air","java"]

# Select a random word {it is use to choose one word randomly from the list}
word = random.choice(words)

# Store guessed letters{stores letter guessed by the player}
guessed_letters = []

# Number of wrong guesses{counts incorrect guesses}
wrong_guesses = 0

# Maximum wrong guesses allowed{player gets 6 worng chances}
max_wrong_guesses = 6

print("🎮 Welcome to Hangman Game!")

while wrong_guesses < max_wrong_guesses:

    display_word = ""

    # Display guessed letters and underscores
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player won
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Get user input
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    # Store guessed letter
    guessed_letters.append(guess)

    # Check correct or wrong guess
    if guess in word:
        print("✅ Correct!")
    else:
        wrong_guesses += 1
        print("❌ Wrong!")
        print("Remaining chances:", max_wrong_guesses - wrong_guesses)

# Game over condition
if wrong_guesses == max_wrong_guesses:
    print("\n💀 Game Over!")
    print("The word was:", word)