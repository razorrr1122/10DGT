# Demonstrate how variables are created and how they work
# Author: Joy Kim
# Date: 11 April 2025
# Version 1.0

# Different types of variables
# Store a number

my_number = 80 # assigning 80 to my_number (variable)
print(my_number)

my_number = 7 # I have reassigned the value of the variable
print(my_number)

# Store a string
name_1 = "Joy"
print(name_1)

# Assign the value of one variable to another
my_number = name_1
print(my_number) # Don't assign values to variables that don't make sense for its name.

# Creating a new variable
num_1 = 5
num_2 = 18

'''Do calculations with variables and atore the result in
# another variables. '''

sum = 5 + 17 # This is not good practice
print(sum)

# Better way
sum1 = num_1 + num_2
print(sum1)

sum_string1 = "18" # This stores a string
sum_string2 = "5" 

# Adding strings together is called concatenation.
sum = sum_string1 + sum_string2
print(sum)
print(sum1)

print("My Calculation for {sum_string1} + {sum_string2} = {sum1}")





