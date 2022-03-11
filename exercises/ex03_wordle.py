"""Wordle function definitions."""
__author__ = "730358329"


def contains_char(user_input: str, char_input: str) -> bool:    # This function checks if a single character input is present anywhere in a word input. If there instances of such, it returns true. If it has checked all indices in the word but found no matches, it returns false. 
    """Functions that checks for equivalence in input for a single character."""
    assert len(char_input) == 1
    index: int = 0
    while index < len(user_input):
        if char_input == user_input[index]:
            return True
        index = index + 1
    return False


def emojified(guess: str, secret: str) -> str:   # This function checks indices of the guess and secret to return a string of emojies indicating type of match.
    """This function return a string of emojies based on different conditions of indices matches."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    result: str = ""
    while index < len(secret):
        if guess[index] == secret[index]:   # Checking the same index in secret and guess.
            result = result + GREEN_BOX 
        elif (contains_char(secret, guess[index])) is False:   # Using contains_char functions to check a single index of the guess against all indices of secret. 
            result = result + WHITE_BOX     # Based on above line, if condition is true, then there is no match and a while box will be added to string, if it is not true, then there is a mismatch and a yellow box is added. 
        else:
            result = result + YELLOW_BOX
        index = index + 1
    return result 
        

def input_guess(exp_len: int) -> str:    # This function ensures that the length of the guess equals the desrired length. 
    """This functions asks user for guess and checks the length of guess against the desired length."""
    guess: str = input(f"Enter a {exp_len} character word: ")
    while len(guess) != exp_len:
        guess = input(f"That wasn't {exp_len} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turns_left: int = 1
    win: bool = False
    while turns_left < 7 and not win:   # If both conditions are true, then the user has not won and has not finished the game. 
        print(f"=== Turn {turns_left}/6 ===")
        guess: str = input_guess(len(secret))   # Using the input_guess functions, which asks user for a guess, to initlalize the guess variable here and check for lenght.
        print(emojified(guess, secret))    # Checking for matches. 
        if guess == secret:
            win = True
        else:
            turns_left = turns_left + 1
    if win is True:
        print(f"You won in {turns_left}/6 turns!")
    else: 
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
       