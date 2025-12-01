# ============================================================
#                PYTHON ASSIGNMENT – 10 EXERCISES
# ============================================================


# --------------------------
# EXERCISE 1
# --------------------------
def exercise1():
    print("\n--- Running Exercise 1 ---")
    # Exercise 1: Print Current Date and Time
    # ----------------------------------------------------------
    from datetime import datetime
    now = datetime.now()
    print("Current date and time:", now)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 2
# --------------------------
def exercise2():
    print("\n--- Running Exercise 2 ---")
    # Exercise 2: Convert String Into Datetime Object
    # Write a code to convert the given date in string format into a Python DateTime object.
    # ----------------------------------------------------------
    
    date_string = "Feb 25 2020 4:20PM"
    from datetime import datetime
    date_object = datetime.strptime(date_string, "%b %d %Y %I:%M%p")
    print("Date string:", date_string)
    print("Converted DateTime object:", date_object)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 3
# --------------------------
def exercise3():
    print("\n--- Running Exercise 3 ---")
    # Exercise 3: Subtract a Week From a Given Date
    # Write a code to subtract a week (7 days) from a given date.
    # ----------------------------------------------------------
    
    import datetime
    from datetime import datetime, timedelta

    given_date = datetime(2020, 2, 25)
    print("Given date:", given_date)

    # subtracting 7 days from given date
    new_date = given_date - timedelta(days=7)

    # printing the new date
    print("Date after subtracting 7 days:", new_date)



    # ----------------------------------------------------------



# --------------------------
# EXERCISE 4
# --------------------------
def exercise4():
    print("\n--- Running Exercise 4 ---")
    # Exercise 4: Format DateTime
    # Write a code to print date in the following format.
    # Day_name  Day_number  Month_name  Year

    # ----------------------------------------------------------
    import datetime
    from datetime import datetime

    now = datetime.now()
    formatted_date = now.strftime("%A %d %B %Y")
    print("Formatted date:", formatted_date)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 5
# --------------------------
def exercise5():
    print("\n--- Running Exercise 5 ---")
    # Exercise 5: Find Day of Week
    # Write a code to find the day of the week of a given date.
    # ----------------------------------------------------------
    
    import datetime
    from datetime import datetime

    given_date = datetime(2020, 7, 26)
    day_of_week = given_date.strftime("%A")
    print("Given date:", given_date)
    print("Day of the week:", day_of_week)


    # ----------------------------------------------------------



# --------------------------
# EXERCISE 6
# --------------------------
def exercise6():
    print("\n--- Running Exercise 6 ---")
    # Exercise 6: Add Week to Given Date
    # Write a code to add a week (7 days) and 12 hours to a given date.
    # ----------------------------------------------------------
    import datetime
    from datetime import datetime, timedelta

    given_date = datetime(2020, 3, 22, 10, 0, 0)
    print("Given date:", given_date)

    # adding 7 days and 12 hours to given date
    new_date = given_date + timedelta(days=7, hours=12)

    # printing the new date
    print("Date after adding 7 days and 12 hours:", new_date)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 7
# --------------------------
def exercise7():
    print("\n--- Running Exercise 7 ---")
    # Exercise 9: Calculate the date 4 months from the current date
    # ----------------------------------------------------------
    import datetime
    from datetime import datetime
    from dateutil.relativedelta import relativedelta

    # we used relativedelta as we cannot use timedelta as it does not support months


    current_date = datetime.now()

    # printing the current date
    print("Current date:", current_date)

    # calculating the date 4 months from the current date
    new_date = current_date + relativedelta(months=4)
    print("Date after 4 months:", new_date)


    # ----------------------------------------------------------



# --------------------------
# EXERCISE 8
# --------------------------
def exercise8():
    print("\n--- Running Exercise 8 ---")
    # Exercise 10: Calculate Days Between Two Dates
    # Write a code to calculate the days between two dates.
    # ----------------------------------------------------------
    
    import datetime
    from datetime import datetime

    date_1 = datetime(2020, 2, 25)
    date_2 = datetime(2020, 9, 17)

    # calculating the difference between two dates
    difference = date_2 - date_1
    print("Date 1:", date_1)
    print("Date 2:", date_2)
    print("Days between two dates:", difference.days)


    # ----------------------------------------------------------



# --------------------------
# EXERCISE 9
# --------------------------
def exercise9():
    print("\n--- Running Exercise 9 ---")
    # Write your Exercise 9 code below
    # ----------------------------------------------------------
    # Your code here
    # ----------------------------------------------------------



# --------------------------
# EXERCISE 10
# --------------------------
def exercise10():
    print("\n--- Running Exercise 10 ---")
    # Write your Exercise 10 code below
    # ----------------------------------------------------------
    # Your code here
    # ----------------------------------------------------------



# ============================================================
# CHOOSE WHICH EXERCISE TO RUN
# ============================================================

if __name__ == "__main__":
    # Change this number to run a different exercise (1–10)
    exercise_to_run = 8

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
