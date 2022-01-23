"""EX01 -Chardle- A cute step towards Wordle."""
_author_ = 730358329

five_character_word: str = input("Enter a 5-character word: ")
if len(five_character_word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
   single_character: str = input("Enter a single character: ")
print("Searching for " + single_character + " in " + five_character_word)
x: int = 0

if single_character == five_character_word[0]:
    print(single_character + " found at index 0")
    x = x + 1
else:
    x = x
if single_character == five_character_word[1]:
    print(single_character + " found at index 1")   
    x = x+ 1
else:
    x == x
if single_character == five_character_word[2]:
    print(single_character + " found at index 2")
    x= x+ 1
else:
    x = x
if single_character == five_character_word[3]:
    print(single_character + " found at index 3")
    x = x+ 1
else: 
    x = x
if single_character == five_character_word[4]:
    print(single_character + " found at index 4")
    x = x + 1
else: 
    x = x 
if x > 0:
    print(str(x) + " instances found")
else:
    print(" no instances found")



    







