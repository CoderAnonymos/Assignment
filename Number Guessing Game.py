import random

class NumberGuessingGame:
    def __init__(self, lower_limit, upper_limit, max_attempts):
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.max_attempts = max_attempts
        self.target_number = random.randint(lower_limit, upper_limit)
        self.attempts = []
        self.guess_stats = {"low": set(), "high": set()}

    def make_guess(self, guess):
        if guess < self.lower_limit or guess > self.upper_limit:
            return f"Your guess must be between {self.lower_limit} and {self.upper_limit}."
        
        self.attempts.append(guess)
        
        if guess == self.target_number:
            return "Congratulations! You've guessed the correct number."
        elif guess < self.target_number:
            self.guess_stats["low"].add(guess)
            return "Too low! Try again."
        else:
            self.guess_stats["high"].add(guess)
            return "Too high! Try again."

    def attempts_remaining(self):
        return self.max_attempts - len(self.attempts)

    def has_attempts_left(self):
        return len(self.attempts) < self.max_attempts

    def get_attempts(self):
        return tuple(self.attempts)

    def get_guess_stats(self):
        return self.guess_stats

    def reveal_answer(self):
        return self.target_number

# Example game loop
def play_game():
    print("Welcome to the Number Guessing Game!")

    try:
        lower_limit = int(input("Enter the lower limit: "))
        upper_limit = int(input("Enter the upper limit: "))
        max_attempts = int(input("Enter the maximum number of attempts: "))
    except ValueError:
        print("Invalid input. Please ensure you enter integers only.")
        return

    game = NumberGuessingGame(lower_limit, upper_limit, max_attempts)

    print(f"I'm thinking of a number between {lower_limit} and {upper_limit}. You have {max_attempts} attempts to guess it.")

    while game.has_attempts_left():
        try:
            guess = int(input("Make your guess: "))
            feedback = game.make_guess(guess)
            print(feedback)

            if feedback.startswith("Congratulations"):
                break
        except ValueError:
            print("Please enter a valid number.")

        print(f"Attempts remaining: {game.attempts_remaining()}\n")

    if not game.has_attempts_left() and game.reveal_answer() not in game.get_attempts():
        print(f"Sorry, you're out of attempts. The correct number was {game.reveal_answer()}.")

    print("Here are your guesses:")
    print(f"All guesses (tuple): {game.get_attempts()}")
    print(f"Low guesses (set): {game.get_guess_stats()['low']}")
    print(f"High guesses (set): {game.get_guess_stats()['high']}")
    print("Game over!")

if __name__ == "__main__":
    try:
        play_game()
    except OSError:
        print("Interactive input is not supported in this environment. Please use a different setup.")
