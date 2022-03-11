"""Example of writing a function to search a list."""

def main() -> None:
    guess: str = input("What is the code word?")
    possible_answers: list[str] = ["pokeman", "wordle"]
    if contains(guess, possible_answers):
        print("We are letting the secret club...")
    else:
        print("Go back to Davis")

#-  Defone a function named contains
# parameters:
#  1. needle - the str we are searching for 
#   2. haystack- the list of the str values we are searcbing for 
def contains(needle: str, haystack: list[str]) -> bool:
# Algorithm: srarch for item in haystack:
#      test if equal to needle 
    for item in haystack:
        if item == needle:
            return True 
    return False

print(__name__)
if __name__ == "__main__": 
   main()