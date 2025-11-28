# ===========================================================================================
#                PYTHON DATA STRUCTURES ASSIGNMENT – 10 EXERCISES
# ===========================================================================================


# --------------------------
# EXERCISE 1
# --------------------------
def exercise1():
    print("\n--- Running Exercise 1 ---")
    # Exercise 1: Given two lists, l1 and l2, write a program to create a third list l3
    # ... by picking an odd-index element from the list l1 and even index elements from the list l2.
    # ----------------------------------------------------------


    list1 = [34, 54, 67, 89, 11, 43, 94]
    list2 = [1, 3, 5, 7, 9, 11, 13]

    print("List 1:", list1)
    print("List 2:", list2)
    print("List with odd-index elements from List 1")
    i = list1[1::2]
    print(i)
    print("List with even-index elements from List 2")
    j = list2[0::2]
    print(j)
    print("Final List:", i + j)
    # ----------------------------------------------------------



# --------------------------
# EXERCISE 2
# --------------------------
def exercise2():
    print("\n--- Running Exercise 2 ---")
    # Exercise 2: Program to remove the item present at index 4 and add it to the 2nd position and at the end of the list
    # ----------------------------------------------------------

    list1 = [54, 44, 27, 79, 91, 41]
    print("Original List:", list1)
    print("List after removing item at index 4: ")

    # pop(index) method removes and returns the item at the given index
    item = list1.pop(4)
    print(list1)

    print("List after adding number at index 2: ")

    # insert(index, item) adds the item at the specified position(index) in the list
    list1.insert(2, 11)
    print(list1)

    print("List after re-adding removed number to the end: of the list")

    # append(item) adds item at the end of the list.
    list1.append(item)
    print("Modified List:", list1)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 3
# --------------------------
def exercise3():
    print("\n--- Running Exercise 3 ---")
    # Exercise 3: Slicing list into 3 equal chunks and reverse each chunk
    # ----------------------------------------------------------
    sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    print("Original List:", sample_list)
    print("Slicing list into 3 equal chunks")

    # determining the size of each chunk by dividing length of list by 3
    chunk_size = len(sample_list) // 3

    # using for loop and list comprehension to create chunks
    chunks = [sample_list[i:i + chunk_size] for i in range(0, len(sample_list), chunk_size)]
    print("Chunks:", chunks)
    print("Reversing each chunk")

    # using slice() to reverse each chunk
    reversed_chunks = [chunk[::-1] for chunk in chunks]
    print("Reversed Chunks:", reversed_chunks)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 4
# --------------------------
def exercise4():
    print("\n--- Running Exercise 4 ---")
    # Exercise 4: Counting the occurrence of each element from a list
    # Write a program to iterate a given list and count the occurrence of each element
    # ... and create a dictionary to show the count of each element.
    # ----------------------------------------------------------
    sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    print("Original List:", sample_list)

    # Creating an empty dictionary to store the count of each element
    count_dict = {}

    # Using a for loop to iterate through sample_list
    for item in sample_list:

        # If the item is already in the dictionary, increment its count
        # Otherwise, add the item to the dictionary with a count of 1
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    print("Element Count Dictionary:", count_dict)
    # ----------------------------------------------------------



# --------------------------
# EXERCISE 5
# --------------------------
def exercise5():
    print("\n--- Running Exercise 5 ---")
    # Exercise 5: Paired Elements from Two Lists as a Set
    # Write a code to create a Python set such that it shows the element from both lists in a pair.
    # ----------------------------------------------------------
    first_list = [2, 3, 4, 5, 6, 7, 8]
    second_list = [4, 9, 16, 25, 36, 49, 64]
    print("First List:", first_list)
    print("Second List:", second_list)

    # Creating an empty set to store paired elements
    paired_set = set()

    # Using a for loop to iterate through both lists
    for i in range(len(first_list)):

        # Adding paired elements as tuples to the set
        paired_set.add((first_list[i], second_list[i]))
    print("Paired Set:", paired_set)

    print("----------------------------------------------------------")
    print("\nUsing zip() to achieve the same result:")

    third_list = [2, 3, 4, 5, 6, 7, 8]
    fourth_list = [4, 9, 16, 25, 36, 49, 64]
    print("Third List:", third_list)
    print("Fourth List:", fourth_list)

    # Using zip() to pair elements from both lists and returning in order of occurrence
    # PS... Python sets are unordered collections, so the order of elements may vary
    # Hence using list to display the paired elements in order
    paired_set2 = list(zip(third_list, fourth_list))
    print("Paired Set using zip():", paired_set2)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 6
# --------------------------
def exercise6():
    print("\n--- Running Exercise 6 ---")
    # Exercise 6: Set Intersection and Removal
    # Write a code to find the intersection (common) of two sets and remove those elements from the first set.
    # ----------------------------------------------------------
    first_set = {23, 42, 65, 57, 78, 83, 29}
    second_set = {57, 83, 29, 67, 73, 43, 48}
    print("First Set:", first_set)
    print("Second Set:", second_set)

    # Finding intersection of both sets using & operator
    intersection = first_set & second_set
    print("Intersection of both sets:", intersection)

    # Removing intersection elements from the first set using difference_update() method
    first_set.difference_update(intersection)
    print("First Set after removing intersection elements:", first_set)


    # removing intersection elements from the first set using -= operator
    first_set = {23, 42, 65, 57, 78, 83, 29}  # resetting first_set
    first_set -= intersection
    print("First Set after removing intersection elements using -= operator:", first_set)


    # using remove() method in a loop to remove intersection elements from the first set
    first_set = {23, 42, 65, 57, 78, 83, 29}  # resetting first_set
    for item in intersection:
        first_set.remove(item)
    print("First Set after removing intersection elements using remove() method:", first_set)
    # ----------------------------------------------------------



# --------------------------
# EXERCISE 7
# --------------------------
def exercise7():
    print("\n--- Running Exercise 7 ---")
    # Exercise 7: Subset or Superset of another set
    # Write a code to checks if one set is a subset or superset of another set. If found, delete all elements from that set.
    # ----------------------------------------------------------
    first_set = {27, 43, 34}
    second_set = {34, 93, 22, 27, 43, 53, 48}
    print("First Set:", first_set)
    print("Second Set:", second_set)
    # Checking if first_set is a subset of second_set
    if first_set.issubset(second_set):
        print("First Set is a subset of Second Set.")
        first_set.clear()  # Deleting all elements from first_set
        print("First Set after deletion:", first_set)
    # Checking if second_set is a superset of first_set
    elif second_set.issuperset(first_set):
        print("Second Set is a superset of First Set.")
        second_set.clear()  # Deleting all elements from second_set
        print("Second Set after deletion:", second_set)
    else:
        print("Neither set is a subset or superset of the other.")
    # ----------------------------------------------------------



# --------------------------
# EXERCISE 8
# --------------------------
def exercise8():
    print("\n--- Running Exercise 8 ---")
    # Exercise 8: Filter List Against Dictionary Values
    # Write a program to iterate a given list and check if a given element exists as a key’s value in a dictionary. 
    # If not, delete it from the list
    # ----------------------------------------------------------
    roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
    sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
    print("Original Roll Number List:", roll_number)
    print("Sample Dictionary:", sample_dict)

    # Using list comprehension to filter roll_number list
    filtered_roll_number = [num for num in roll_number if num in sample_dict.values()]
    print("Filtered Roll Number List:", filtered_roll_number)

    # ----------------------------------------------------------
    print("--- Alternative Method ---")
    # Using a for loop to remove elements not in dictionary values
    roll_number = [47, 64, 69, 37, 76, 83, 95, 97]  # resetting roll_number list
    for num in roll_number[:]:  # iterating over a copy of the list
        # Removing num if it's not in the dictionary values
        if num not in sample_dict.values():
            roll_number.remove(num)
    print("Filtered Roll Number List using for loop:", roll_number)
    # ----------------------------------------------------------



# --------------------------
# EXERCISE 9
# --------------------------
def exercise9():
    print("\n--- Running Exercise 9 ---")
    # Exercise 9: Extract Unique Dictionary Values to List
    # Write a code to get all values from the dictionary and add them to a list but don’t add duplicates
    # ----------------------------------------------------------
    speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
    print("Original Dictionary:", speed)
    # Using set to extract unique values from the dictionary
    unique_values = set(speed.values())
    # Converting set back to list
    unique_list = list(unique_values)
    print("List of Unique Values:", unique_list)

    print("--- Alternative Method ---")
    # Using a for loop to extract unique values
    unique_list2 = []
    for value in speed.values():
        if value not in unique_list2:
            unique_list2.append(value)
    print("List of Unique Values using for loop:", unique_list2)
    # ----------------------------------------------------------



# --------------------------
# EXERCISE 10
# --------------------------
def exercise10():
    print("\n--- Running Exercise 10 ---")
    # Exercise 10: remove duplicates from a list
    # Write a code to remove duplicates from a list and create a tuple and find the minimum and maximum number
    # ----------------------------------------------------------
    sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
    print("Original List:", sample_list)

    # using for loop to remove duplicates
    unique_list = []
    for item in sample_list:
        if item not in unique_list:
            unique_list.append(item)
    print("List after removing duplicates:", unique_list)

    # converting list to tuple
    unique_tuple = tuple(unique_list)
    print("Tuple:", unique_tuple)

    # finding minimum and maximum number in the tuple
    min_value = min(unique_tuple)
    max_value = max(unique_tuple)
    print("Minimum Value in Tuple:", min_value)
    print("Maximum Value in Tuple:", max_value)


    print("--- Alternative Method ---")
    # using set to remove duplicates
    # Sets automatically remove duplicates as they do not allow duplicate values
    
    unique_list2 = list(set(sample_list))
    print("List after removing duplicates using set:", unique_list2)
    # converting list to tuple
    unique_tuple2 = tuple(unique_list2)
    print("Tuple using set:", unique_tuple2)
    # finding minimum and maximum number in the tuple
    min_value2 = min(unique_tuple2)
    max_value2 = max(unique_tuple2)
    print("Minimum Value in Tuple using set:", min_value2)
    print("Maximum Value in Tuple using set:", max_value2)
    # ----------------------------------------------------------



# ============================================================
# CHOOSE WHICH EXERCISE TO RUN
# ============================================================

if __name__ == "__main__":
    # Change this number to run a different exercise (1–10)
    exercise_to_run = 10

    # Mapping exercise number to the function
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
        10: exercise10
    }

    # Run the selected exercise
    if exercise_to_run in exercises:
        exercises[exercise_to_run]()
    else:
        print(f"Invalid choice: {exercise_to_run}. Choose a number between 1 and 10.")
