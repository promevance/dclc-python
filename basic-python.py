# basic python code to multiply two numbers and check the result
a = 400
b = 25
if a*b<=1000:
    print ("The result is:", a*b)
else :
    print ("The result is:", a+b)



# basic python code to output a range and then add a number to each element in the range

    print ("Printing current and previous number sum in a range(10)")
    previous_num = 0
    # Iterate through a range of 10
    for i in range(1, 11):
           x_sum = previous_num + i
           print ("Current Number is :", i, "Previous Number is :", previous_num, "Sum is:", x_sum)
           previous_num = i


# basic python code to pull out the letters in a string at even index positions
input_str = input("Enter any word here: ")

print ("Original String is: ", input_str)
print ("Letters in even index positions are: ")
for i in range(0, len(input_str)):
    if i%2==0:
        print (input_str[i])


# basic python code to remove first n characters from a string
def remove_chars(str, n):
    # Removing first n characters from the string
    new_str = str[n:]
    return new_str
input_str = input("Enter any word here: ")
n = int(input("Enter number of characters to remove from start: "))
result_str = remove_chars(input_str, n)
print ("String after removing first", n, "characters is:", result_str)

