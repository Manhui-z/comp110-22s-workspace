"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730442764"


five_char_word: str = input("Enter a 5-character word: ")
if len(five_char_word) != 5:
    print("Error: word must contain 5 characters")
    exit()

enter_a_char: str = input("Enter a single character: ")
if len(enter_a_char) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Search for " + enter_a_char + " in " + five_char_word)

times: int = 0

if enter_a_char == five_char_word[0]:
    print(enter_a_char + " found at index 0")
    times = times + 1

if enter_a_char == five_char_word[1]:
    print(enter_a_char + " found at index 1")
    times = times + 1

if enter_a_char == five_char_word[2]:
    print(enter_a_char + " found at index 2")
    times = times + 1

if enter_a_char == five_char_word[3]:
    print(enter_a_char + " found at index 3")
    times = times + 1

if enter_a_char == five_char_word[4]:
    print(enter_a_char + " found ar index 4")
    times = times + 1

if times == 0:
    print("No instances of " + enter_a_char + " found in " + five_char_word)
else:
    if times == 1:
        print(str(times) + " instance of " + enter_a_char + " found in " + five_char_word)
    else:
        print(str(times) + " instances of " + enter_a_char + " found in " + five_char_word)