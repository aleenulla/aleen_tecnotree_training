import random

# List of city
words = ["mumbai", "kolkolata", "bangalore", "mysore", "delhi", "chennai"]
print("---------Guess the Word (hint : City Names)-----")

secret_word = random.choice(words)  # Choose a random secret word

# Set up the game
progress = ["_" for letter in secret_word]
missed_letters = []
num_guesses = 0
max_guesses = 6

# Main game loop
while "_" in progress and num_guesses < max_guesses:
    print("*******************************")
    print("Secret word: " + " ".join(progress))
    print("Missed letters: " + ", ".join(missed_letters))  #.join bulit-in method used for join the elements in list
    guess = input("Guess a letter: ").lower()
    # Check if the guess is correct
    if guess in secret_word:
        # Update the progress
        for i, letter in enumerate(secret_word):
            if letter == guess:
                progress[i] = guess
    else:
        # Add the missed letter to the list
        missed_letters.append(guess)
        # Increment the number of guesses
        num_guesses += 1

# Check if the player won or lost
if "_" not in progress:
    print("You win! The secret word was " + secret_word +" 🥳🥳🎉🎉")
else:
    print("You lose! The secret word was " + secret_word+ " ☹️")
