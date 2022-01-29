"""EX02 - One Short Wordle."""

__author__ = "730442764"

secret: str = "python"
secret_len: int = (len(secret))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
alt_i: int = 0
guess_emoji: str = ""
alternate_emoji: str = ""


guess: str = input(f"What is your {secret_len}-letter guess? ")

while len(guess) != secret_len:
    guess = input(f"That was not {secret_len} letters! Try again: ")
# continue until the length of guess equal to length of secret

if len(guess) == secret_len and guess != secret:
    while i < len(guess):
        if guess[i] == secret[i]:
            guess_emoji += GREEN_BOX    
            # Test if the character of guess of that index is exactly equalt to the character of secrect of the same index
        else:
            guess_bol: bool = False
            alt_i = 0
            while guess_bol is not True and alt_i < secret_len:
                # if the character of the guess exist in the guess 
                if guess[i] == secret[alt_i]:
                    guess_bol = True       
                alt_i = alt_i + 1
            if guess_bol is True:
                guess_emoji += YELLOW_BOX
            else:
                guess_emoji += WHITE_BOX
        i = i + 1
    print(guess_emoji)
    print("Not quite. Play again soon!")

elif len(guess) == len(secret) and guess == secret:
    while i < 6:
        guess_emoji += GREEN_BOX
        i = i + 1
    print(guess_emoji)
    print("Woo! You got it!")
# if the guess is the secrect, then print "Woo! You got it!"