""""Examples of using lists in a simple game. """


from random import randint

rolls: list[int] = list()

while rolls[len(rolls) - 1 ] != 1: 
    rolls.append(randint(1, 6))
    

# rolls: list[int] = list()  # square brackets indicate that we have a list of some type, and the brackets separate the values in the list
# # The list() is an empty list 
# rolls.append(randint(1, 6))   # Method call 
# rolls.append(randint(1, 6))   # Appending items to a list adds it to the end 
# print(rolls)

# #  Access an individual item
# print(rolls[0])
# print(rolls[1])

# # Acess length of list
# print(len(rolls))

# # Acess last item of a list
# print(rolls[len(rolls) - 1])

# # or last_index: int = len(rolls) - 1
# # print(rolls[last_index])

