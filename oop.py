# ============================================================
#                PYTHON ASSIGNMENT – 10 EXERCISES
# ============================================================


# --------------------------
# EXERCISE 1
# --------------------------
def exercise1():
    print("\n--- Running Exercise 1 ---")
    # OOP Exercise 1: Create a Class with instance attributes
    # Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
    # ----------------------------------------------------------
    
    class Vehicle:
        def __init__(self, max_speed, mileage):
            self.max_speed = max_speed
            self.mileage = mileage

    # creating an instance of Vehicle
    car = Vehicle(240, 18)
    print("Vehicle max speed:", car.max_speed)
    print("Vehicle mileage:", car.mileage)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 2
# --------------------------
def exercise2():
    print("\n--- Running Exercise 2 ---")
    # OOP Exercise 2: Create a Vehicle class without any variables and methods
    # ----------------------------------------------------------
    
    class Vehicle:
        pass

    # creating an instance of Vehicle
    my_vehicle = Vehicle()
    print("Vehicle instance created:", my_vehicle)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 3
# --------------------------
def exercise3():
    print("\n--- Running Exercise 3 ---")
    # OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
    # Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.
    # ----------------------------------------------------------
    class Vehicle:

        def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage

    class Bus(Vehicle):
        pass

    # creating an instance of Bus
    school_bus = Bus("School Volvo", 180, 12)
    print("Bus Name:", school_bus.name)
    print("Bus Max Speed:", school_bus.max_speed)
    print("Bus Mileage:", school_bus.mileage)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 4
# --------------------------
def exercise4():
    print("\n--- Running Exercise 4 ---")
    # OOP Exercise 4: Class Inheritance
    # Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50
    # ----------------------------------------------------------
    
    class Vehicle:
        def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage

        def seating_capacity(self, capacity):
            return f"The seating capacity of a {self.name} is {capacity} passengers"
        
    class Bus(Vehicle):
        def seating_capacity(self, capacity=50):
            return super().seating_capacity(capacity)
        
    # creating an instance of Bus
    school_bus = Bus("School Volvo", 180, 12)

    print(school_bus.seating_capacity())

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 5
# --------------------------
def exercise5():
    print("\n--- Running Exercise 5 ---")
    # OOP Exercise 5: Define a property that must have the same value for every class instance (object)
    # Define a class attribute "color" with a default value white. I.e., Every Vehicle should be white.
    # ----------------------------------------------------------
    
    class Vehicle:

        def __init__(self, name, max_speed, mileage):
            self.name = name
            self.max_speed = max_speed
            self.mileage = mileage

    class Bus(Vehicle):
        pass

    class Car(Vehicle):
        pass

    # creating instances of Bus and Car
    school_bus = Bus("School Volvo", 180, 12)
    family_car = Car("Family Honda", 200, 15)

    # setting the color attribute for both instances
    school_bus.color = "White"
    family_car.color = "White"

    print("Bus Color:", school_bus.color)
    print("Car Color:", family_car.color)

    #printing all class attributes for both instances
    print("Bus attributes:", school_bus.__dict__)
    print("Car attributes:", family_car.__dict__)


    # ----------------------------------------------------------



# --------------------------
# EXERCISE 6
# --------------------------
def exercise6():
    print("\n--- Running Exercise 6 ---")
    # OOP Exercise 6: Class Inheritance
    # Create a Bus child class that inherits from the Vehicle class. We need to access the parent class from within a method of a child class.
    # The default fare charge for any vehicle is its seating capacity multiplied by 100 (seating capacity * 100).
    # If the vehicle is a Bus instance, we need to add an extra 10% to the full fare as a maintenance charge... 
    # Therefore, the total fare for a Bus instance will be the final amount, calculated as total fare plus 10% of the total fare... 
    # (final amount = total fare + 10% of the total fare.)
    # Note: The bus seating capacity is 50, so the final fare amount should be 5500
    # ----------------------------------------------------------
    
    class Vehicle:
        def __init__(self, name, mileage, capacity):
            self.name = name
            self.mileage = mileage
            self.capacity = capacity

        def fare(self):
            return self.capacity * 100

    class Bus(Vehicle):
        def fare(self):

            # getting the total fare from the parent class
            total_fare = super().fare()

            # adding 10% maintenance charge for Bus
            total_fare += total_fare * 0.10
            return total_fare

    School_bus = Bus("School Volvo", 12, 50)
    print("Total Bus fare is:", School_bus.fare())
    # ----------------------------------------------------------



# --------------------------
# EXERCISE 7
# --------------------------
def exercise7():
    print("\n--- Running Exercise 7 ---")
    # OOP Exercise 7: Check type of an object
    # Write a program to determine which class a given Bus object belongs to.
    # ----------------------------------------------------------
    
    class Vehicle:
        def __init__(self, name, mileage, capacity):
            self.name = name
            self.mileage = mileage
            self.capacity = capacity

    class Bus(Vehicle):
        pass

    School_bus = Bus("School Volvo", 12, 50)

    # checking the type of the object
    print("The class of the object School_bus is:", type(School_bus))

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 8
# --------------------------
def exercise8():
    print("\n--- Running Exercise 8 ---")
    # OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class
    # ----------------------------------------------------------
    
    class Vehicle:
        def __init__(self, name, mileage, capacity):
            self.name = name
            self.mileage = mileage
            self.capacity = capacity

    class Bus(Vehicle):
        pass

    School_bus = Bus("School Volvo", 12, 50)

    # checking if School_bus is an instance of Vehicle
    is_instance = isinstance(School_bus, Vehicle)
    print("Is School_bus an instance of Vehicle?", is_instance)

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 9
# --------------------------
def exercise9():
    print("\n--- Running Exercise 9 ---")
    # OOP Exercise 9: Check object is a subclass of a particular class
    # Write a code to check the following
        # Dog is a subclass of Animal? –> True
        # Animal is a subclass of Dog? –> False
        # Cat is a subclass of Animal? –> False
        # Puppy is a subclass of Animal –> True
    # ----------------------------------------------------------

    class Animal:
        pass

    class Dog(Animal):
        pass

    class Puppy(Dog):
        pass

    class Cat:
        pass

    print("Is Dog a subclass of Animal?", issubclass(Dog, Animal))
    print("Is Animal a subclass of Dog?", issubclass(Animal, Dog))
    print("Is Cat a subclass of Animal?", issubclass(Cat, Animal))
    print("Is Puppy a subclass of Animal?", issubclass(Puppy, Animal))

    # ----------------------------------------------------------



# --------------------------
# EXERCISE 10
# --------------------------
def exercise10():
    print("\n--- Running Exercise 10 ---")
    # OOP Exercise 10: Calculate the area of different shapes using OOP
    # You have given a Shape class and subclasses Circle  and Square. The parent class (Shape) has a area() method.
    # Now, Write a OOP code to calculate the area of each shapes (each subclass must write its own implementation of area() method to calculates its area).
    # ----------------------------------------------------------
    
    class Shape:
        def area(self):
            raise NotImplementedError("Area method must be implemented by subclasses")

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14159 * (self.radius ** 2)

    class Square(Shape):
        def __init__(self, side):
            self.side = side

        def area(self):
            return self.side * self.side

    # Example of polymorphism
    shapes = [Circle(5), Square(7), Circle(3)]

    for shape in shapes:
        print(shape.area())  # Output: 78.53975, 49, 28.27431
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
