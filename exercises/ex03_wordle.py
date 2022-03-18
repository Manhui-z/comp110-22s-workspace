"""EX03 Structered Wordle."""

__author__ = "730442764"


# This function is to find whether the character of the guess exist in the secret.
def contains_char(secret: str, guess_char: str) -> bool:
    """Whether the character in guess exist in secret."""
    i: int = 0
    assert len(guess_char) == 1
    while i < len(secret):
        if secret[i] == guess_char:
            return True
        else:
            i += 1
    return False
# If the character of the guess exist in the secret, return True.
# If the character of the guess doesn't exist in the secret, return False.


# This function is to return the result of the previous test.
def emojified(guess: str, secret: str) -> str:
    """Return the emoji about the guess."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    guess_emoji: str = ""
    i: int = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            guess_emoji += GREEN_BOX
        else:
            if contains_char(secret, guess[i]) is True:
                guess_emoji += YELLOW_BOX
            else:
                guess_emoji += WHITE_BOX
        i += 1
    return guess_emoji
# If the character of the guess is exactly the character of the secret in the same index, return Greenbox emoji.
# If the character of the guess is not the character of the secret in the same index but exist in other index of the secret, return Yellowbox emoji.
# If the character of the guess is not included in the secret, return Whitebox emoji.


# This function is to find the the length of the guess is equal to the length of the secret.
def input_guess(expected_len: int) -> str:
    """Whether the guess has the expected length?"""
    guess: str = input(f"Enter a {expected_len} character word: ")
    while len(guess) != expected_len:
        guess = input(f"That wasn't {expected_len} chars! Try again: ")
    return guess
# The while loop will always go until the length of the guess equal to the length of the secret.


# This function is to show your guess of each turn, and which turn you get the secret, or you use up all the turns but doesn't get the secret.
# This function also connect all the previous function to combine the result of them.
def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    secret: str = "codes"
    GREEN_BOX: str = "\U0001F7E9"
    while turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        if emojified(guess, secret) == GREEN_BOX * len(secret):
            print(emojified(guess, secret))
            print(f"You won in {turn}/6 turns!")
            return             
        else:
            print(emojified(guess, secret))
            turn += 1
    print("X/6 - Sorry, try again tomorrow!")


# Enable the program to run as a module, and enable other modules to import these functions
if __name__ == "__main__":
    main()