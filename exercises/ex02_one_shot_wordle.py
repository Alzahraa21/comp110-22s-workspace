"""EX02 One Shot Wordle Loops."""
__author__ = "730358329"

SECRET: str = "python"
guess: str = input(f"What is your {len(SECRET)} letter guess? ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index_tracker: int = 0
result: str = " "

while len(guess) != len(SECRET):  # will continue looping until length of guess and secret are equal
    guess = input(f"that was not {len(SECRET)}! Try again: ")

while index_tracker < len(SECRET):  # will continue looping until the relation is false
    if guess[index_tracker] == SECRET[index_tracker]:  # if the same indices have the same character, program will add a green box to the result string
        result = result + GREEN_BOX
    else: 
        alternate_index: int = 0
        another_place: bool = False
        while another_place is False and alternate_index < len(SECRET):  # if the indices are not the same, program tests the index we are in the secret with an alternate index in the guess starting at 0
            if SECRET[alternate_index] == guess[index_tracker]:
                another_place = True  # if statement above is true, the another place bool will become true and it will go to line 28 where a yellow box will be added to result string
            else:
                alternate_index = alternate_index + 1  # if statement above is not true, program will increase the alternate index by one and test it again with the same index in the secret from where the loop started
        if another_place is True:
            result = result + YELLOW_BOX
        else: 
            result = result + WHITE_BOX  # if another place was false for the particular guess index, then it will add a white box to the result string
    index_tracker = index_tracker + 1  # after the another place while loop is done for a particular secret index, the index tracker will increaase by one and the same steps as above will continue until the relational statement in the big loop is false
print(result)  # this is at this index so it does not print results everytime the loop goes through
        

if guess == SECRET:
    print("Woo! You got it")
else:
    print("Not quite. Play again later")