"""
This is a Secret Santa Generator written in python.
The user is prompted to give a list of names
The program randomly assigns each person their Secret Santa
The user is given the option to re-shuffle the Secret Santa allocations
"""

import random


def combination_generator(names):
    index_counter = []
    random_index = None
    position_counter = 0

    for santa in names:
        # Generates a random number which will be used to identify a recipient
        random_index = random.randint(0, len(names)-1)

        """
        Logic check to see if the index number has been used already or
        if it the santa and recipient are the same person
        """

        while random_index in index_counter or random_index == position_counter:
            random_index = random.randint(0, len(names)-1)

        recipient = names[random_index]
        print(f"\t{santa.capitalize()} is {recipient.capitalize()}'s Secret Santa")

        position_counter += 1
        index_counter.append(random_index)


print("*"*40)
print("Welcome to the Secret Santa Generator!")
print("*"*40, "\n")


names_list = []
number_of_names = 1


user_input = input("Please enter a name: ")
names_list.append(user_input.lower())


while True:
    user_input = input("Please enter another name or enter 'Done' to finish: ")
    if number_of_names > 2 and user_input.lower() == "done":
        break
    elif number_of_names <= 2 and user_input.lower() == "done":
        print("You need at least 3 people to play this game!")
        continue
    elif user_input.lower() in names_list:
        continue
    else:
        names_list.append(user_input.lower())
        number_of_names += 1


print("\nHere is your list of Secret Santa's: ")
combination_generator(names_list)


user_satisfied = False


while not user_satisfied:
    reshuffle_list = input("Would you like to try a different combination? (y/n): ")
    if reshuffle_list.lower() == "y":
        user_satisfied = False
        print("\n")
        combination_generator(names_list)
    else:
        print("\nThank you for using the Secret Santa Generator.\nHave a Merry Christmas!")
        break
