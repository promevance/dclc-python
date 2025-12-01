# ============================================================
#                PYTHON ASSIGNMENT – 20 EXERCISES
# ============================================================


# --------------------------
# EXERCISE 1
# --------------------------
def exercise1():
    print("\n--- Running Exercise 1 ---")
    # Exercise 1: Perform basic dictionary operations
        # Perform following operations on given dictionary
        # Add New Key-Value Pair: Add a new key-value pair, 'profession': 'Doctor', to the dictionary and print the updated dictionary.
        # Modify Value: Change the value of the age key to 40 in the dictionary and print the updated dictionary.
        # Access Key: Print the value associated with the city key.

    my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
    print("Original dictionary:", my_dict)
    # Add a new key-value pair
    my_dict['profession'] = 'Engineer'
    print("After adding profession:", my_dict)
    # Update an existing value
    my_dict['age'] = 40
    print("After updating age:", my_dict)
    # Access a value by key
    print("City:", my_dict['city'])




    # ----------------------------------------------------------



# --------------------------
# EXERCISE 2
# --------------------------
def exercise2():
    print("\n--- Running Exercise 2 ---")
    # Exercise 2: Perform dictionary operations
        # Perform following operations on given dictionary
        # Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
        # Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
        # Check if Key Exists in the dictionary
    
    my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
    print("Original dictionary:", my_dict)

    # removing profession key-value pair
    del my_dict['profession']
    print("After removing profession:", my_dict)

    # Getting all items in the dictionary
    print("Items in the dictionary:")
    for key, value in my_dict.items():
        print(f"{key}: {value}")
    
    # Checking if 'age' key exists
    for key in my_dict.keys():
        if key == 'age':
            print("Key 'age' exists in the dictionary.")
            break


    # ----------------------------------------------------------



# --------------------------
# EXERCISE 3
# --------------------------
def exercise3():
    print("\n--- Running Exercise 3 ---")
    # Exercise 3: Dictionary from Lists
    # Write a Python program to convert two Python lists into a dictionary
    # where elements from the first list become keys and elements from the second list become values.


    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    my_dict = dict(zip(keys, values))
    print("Dictionary created from lists:", my_dict)


    # Alternative method
    my_dict_alt = {}
    for i in range(len(keys)):
        my_dict_alt[keys[i]] = values[i]
    print("Alternative method dictionary:", my_dict_alt)



    # ----------------------------------------------------------



# --------------------------
# EXERCISE 4
# --------------------------
def exercise4():
    print("\n--- Running Exercise 4 ---")
    # Exercise 4: Clear Dictionary
    # Clear all key-value pairs from a given dictionary and print it.

    my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
    print("Original dictionary:", my_dict)
    my_dict.clear()
    print("After clearing:", my_dict)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 5
# --------------------------
def exercise5():
    print("\n--- Running Exercise 5 ---")
    # Exercise 5: Merge two Python dictionaries into one
    # Write a code to merge two dictionaries into a new dictionary and print it.

    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

    # Merging dictionaries
    merged_dict = {**dict1, **dict2}
    print("Merged dictionary:", merged_dict)


    # Using update() method
    print( "Alternative merging using update() method:")
    print("Original dict1:", dict1)
    dict1.update(dict2)
    print("Merged using update():", dict1)


    # Using concatentation in Python 3.9+
    print( "Alternative merging using | operator:")
    merged_dict_alt = dict1 | dict2
    print("Merged using | operator:", merged_dict_alt)


    # ----------------------------------------------------------



# --------------------------
# EXERCISE 6
# --------------------------
def exercise6():
    print("\n--- Running Exercise 6 ---")
    # Exercise 9: Modify Nested Dictionary
    # In the below dictionary, change name to ‘Jessa’.

    nested_student_dict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                    }
                }
            }
        }
    
    print("Original nested dictionary:", nested_student_dict)
    # Modifying the name
    nested_student_dict["class"]["student"]["name"] = "Jessa"

    print("After modification:", nested_student_dict)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 7
# --------------------------
def exercise7():
    print("\n--- Running Exercise 7 ---")
    # Exercise 10: Initialize dictionary with default values
    # In Python, we can initialize the keys with the same values.

    employees = ['Kelly', 'Emma']
    defaults = {"designation": 'Developer', "salary": 8000}
    
    # Initializing dictionary with default values
    employee_dict = dict.fromkeys(employees, defaults)
    print("Initialized dictionary with default values:", employee_dict)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 8
# --------------------------
def exercise8():
    print("\n--- Running Exercise 8 ---")
    # Exercise 1: Perform Basic Tuple Operations
    # Create a Tuple: Create a tuple named my_tuple containing the numbers 1, 2, 3, 4, and 5.
    # Access Elements: Access and print the third element of my_tuple.
    # Tuple Length: Find and print the length of my_tuple.

    my_tuple = (1, 2, 3, 4, 5)
    print("Created tuple:", my_tuple)

    # Accessing the third element
    third_element = my_tuple[2]
    print("Third element:", third_element)

    # Finding the length of the tuple
    tuple_length = len(my_tuple)
    print("Length of the tuple:", tuple_length)


    # ----------------------------------------------------------



# --------------------------
# EXERCISE 9
# --------------------------
def exercise9():
    print("\n--- Running Exercise 9 ---")
    # Exercise 2: Tuple Repetition
    # Repeat a below tuple three times.

    original_tuple = ('a', 'b')
    repeated_tuple = original_tuple * 3
    print("Original tuple:", original_tuple)
    print("Repeated tuple:", repeated_tuple)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 10
# --------------------------
def exercise10():
    print("\n--- Running Exercise 10 ---")
    # Exercise 3: Slicing Tuples
    # Slice below tuple to get elements from the 4th to the 7th position.


    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    sliced_tuple = numbers[3:7]
    print("Original tuple:", numbers)
    print("Sliced tuple (4th to 7th position):", sliced_tuple)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 11
# --------------------------
def exercise11():
    print("\n--- Running Exercise 11 ---")
    # Exercise 4: Reverse the tuple

    tuple1 = (10, 20, 30, 40, 50)
    reversed_tuple = tuple1[::-1]
    print("Original tuple:", tuple1)
    print("Reversed tuple:", reversed_tuple)
    # ----------------------------------------------------------



# --------------------------
# EXERCISE 12
# --------------------------
def exercise12():
    print("\n--- Running Exercise 12 ---")
    # Exercise 5: Access Nested Tuples
    # Write a code to access and print value 20 from given nested tuple.

    tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
    accessed_value = tuple1[1][1]
    print("Original nested tuple:", tuple1)
    print("Accessed value 20:", accessed_value)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 13
# --------------------------
def exercise13():
    print("\n--- Running Exercise 13 ---")
    # Exercise 9: Copy Specific Elements From Tuple
    # Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

    tuple1 = (11, 22, 33, 44, 55, 66)
    new_tuple = (tuple1[3], tuple1[4])
    print("Original tuple:", tuple1)
    print("New tuple with copied elements:", new_tuple)
    # ----------------------------------------------------------



# --------------------------
# EXERCISE 14
# --------------------------
def exercise14():
    print("\n--- Running Exercise 14 ---")
    # Exercise 10: List to Tuple
    # Convert a list my_list = [10, 20, 30] into a tuple

    my_list = [10, 20, 30]
    my_tuple = tuple(my_list)
    print("Original list:", my_list)
    print("Converted tuple:", my_tuple)

    print("Class of my_tuple:", type(my_tuple))
    # ----------------------------------------------------------



# --------------------------
# EXERCISE 15
# --------------------------
def exercise15():
    print("\n--- Running Exercise 15 ---")
    # Your code here
    # ----------------------------------------------------------



# --------------------------
# EXERCISE 16
# --------------------------
def exercise16():
    print("\n--- Running Exercise 16 ---")
    # Your code here
    # ----------------------------------------------------------



# --------------------------
# EXERCISE 17
# --------------------------
def exercise17():
    print("\n--- Running Exercise 17 ---")
    # Your code here
    # ----------------------------------------------------------



# --------------------------
# EXERCISE 18
# --------------------------
def exercise18():
    print("\n--- Running Exercise 18 ---")
    # Your code here
    # ----------------------------------------------------------



# --------------------------
# EXERCISE 19
# --------------------------
def exercise19():
    print("\n--- Running Exercise 19 ---")
    # Your code here
    # ----------------------------------------------------------



# --------------------------
# EXERCISE 20
# --------------------------
def exercise20():
    print("\n--- Running Exercise 20 ---")
    # Your code here
    # ----------------------------------------------------------



# ============================================================
# CHOOSE WHICH EXERCISE TO RUN
# ============================================================

if __name__ == "__main__":
    # Change this number to run a different exercise (1–20)
    exercise_to_run = 14

    # Mapping exercise numbers to functions
    exercises = {
        1: exercise1,
        2: exercise2,
        3: exercise3,
        4: exercise4,
        5: exercise5,
        6: exercise6,
        7: exercise7,
        8: exercise8,
        9: exercise9,
        10: exercise10,
        11: exercise11,
        12: exercise12,
        13: exercise13,
        14: exercise14,
        15: exercise15,
        16: exercise16,
        17: exercise17,
        18: exercise18,
        19: exercise19,
        20: exercise20
    }

    # Run the selected exercise
    if exercise_to_run in exercises:
        exercises[exercise_to_run]()
    else:
        print(f"Invalid choice: {exercise_to_run}. Choose a number between 1 and 20.")
