# Create our Checklist
checklist = list()


# Define Functions
def create(item):
    # Create item code here
    checklist.append(item)


def read(index):
    # Read code here
    item = checklist[index]
    return item


def update(index, item):
    # Update code here
    checklist[index] = item


def destroy(index):
    # Destroy code here
    checklist.pop(index)


def list_all_items():
    index = 0
    for list_item in checklist:
        print(str(index) + list_item)
        index += 1
    # Code to list all items in list


def select(function_code):
    # Create item
    if function_code == "C" or function_code == "c":
        input_item = user_input("Input item:")
        create(input_item)
        return True

    # Read items
    elif function_code == "R" or function_code == "r":
        item_index = user_input("Index Number?")

        item_index = int(item_index)
    # Remember that item_index must actually exist or our program will crash.

        print (read(item_index))
        return True

        # Print all items
    elif function_code == "P" or function_code == "p":
        list_all_items()
        return True

    elif function_code == "Q" or function_code == "q":
        # This is where we want to stop our loop
            return False

        # Catch all
    else:
        print("Unknown Option")
        return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input
    user_input = input(prompt)
    return user_input


# user_value = user_input("Please Enter a value:")
# print(user_value)

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list , and Q to quit")
    running = select(selection)



def test():
    # Your testing code here
    # ...
    # Call your new function with the appropriate value
    select("C")
    # View the results
    list_all_items()
    # Call function with new value
    select("R")
    # View results
    list_all_items

    # Run test
    #test()
