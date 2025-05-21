# Ask user for width and loop until they
# enter a number that is more than zero

def num_check(question):...
# ask the user for a number
while True: 
    width = float(input("Width: ")) 

# check that the number is more than zero
    if width > 0:
        break
    else: 
         print("Please enter a number that is more than zero\n")
         
error = "Please enter a number that is more than zero\n"

print(error)
   
# Main routine Goes Here
for item in range(0, 2):
    width = num_check("Width: ")
    print(width)

print()

for item in range(0, 2):
    height = num_check("Height: ")
    print(height)