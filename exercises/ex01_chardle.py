"""EX01 -Chardle- A cute step towards Wordle."""
__author__ = "730358329"

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) == 5:
    single_character: str = input("Enter a single character: ")
    if len(single_character) != 1: 
        print("Error: Character must be a single character.")
        exit()
else:
    print("Error: Word must contain 5 characters")
    exit()
print("Searching for " + single_character + " in " + five_character_word)
x: int = 0

if single_character == five_character_word[0]:
    print(single_character + " found at index 0")
    x = x + 1
else:
    x = x
if single_character == five_character_word[1]:
    print(single_character + " found at index 1")   
    x = x + 1
else:
    x == x
if single_character == five_character_word[2]:
    print(single_character + " found at index 2")
    x = x + 1
else:
    x = x
if single_character == five_character_word[3]:
    print(single_character + " found at index 3")
    x = x + 1
else: 
    x = x
if single_character == five_character_word[4]:
    print(single_character + " found at index 4")
    x = x + 1
else: 
    x = x 
if x == 1:
    print(str(x) + " instance of " + single_character + " found in " + five_character_word)
else: 
    if x > 1:
        print(str(x) + " instances of " + single_character + " found in " + five_character_word)
    else:
        print("No instances of " + single_character + " found in " + five_character_word)
