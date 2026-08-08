import random
import string

#create a class for the word guessing game
class WordGame:
    def __init__(self, max_lives=6):
        self.words = [
            "python", "variable", "function", "iterator", "notebook",
            "pipeline", "dataset", "computer", "research", "analytics"
        ]

        self.secret_word = random.choice(self.words)
        self.blanks = ["_" for _ in self.secret_word]
        self.lives = max_lives
        self.used_letters = set()
#create a method to get a letter from the user
    def get_letter(self):
        while True:
            guess = input("Guess a letter: ").strip().lower()

            if len(guess) != 1 or guess not in string.ascii_lowercase:
                print("→ Please enter a single A-Z letter.")
                continue

            if guess in self.used_letters:
                print("→ You already tried that letter.")
                continue

            return guess
#create a method to reveal the letters in the secret word
    def reveal_letters(self, letter):
        found = False

        for i, ch in enumerate(self.secret_word):
            if ch == letter:
                self.blanks[i] = letter
                found = True

        return found
#crate a method to play the game
    def play(self):
        print("\nWelcome to Word Guessing!")
        print(f"The word has {len(self.secret_word)} letters.")
        print(" ".join(self.blanks))

        while True:
            guess = self.get_letter()
            self.used_letters.add(guess)

            if self.reveal_letters(guess):
                print("\nWell done! You found a letter.")
                print(" ".join(self.blanks))

                if "_" not in self.blanks:
                    print("\nCongratulations! You guessed the word!")
                    print(f"Word: {self.secret_word}")
                    print("GAME OVER")
                    break

            else:
                self.lives -= 1

                print(f"\nNope! Lives left: {self.lives}")
                print(" ".join(self.blanks))

                if self.lives <= 0:
                    print("\nOut of lives!")
                    print(f"The word was: {self.secret_word}")
                    print("GAME OVER")
                    break


# Start the game
if __name__ == "__main__":
    game = WordGame()
    game.play()