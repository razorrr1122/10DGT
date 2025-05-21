# Ask user for width and loop until they 
# enter a number that is more than zero
def num_check(response):
    while True:
        try:
            value = float(input(response))  
            return value                
        except ValueError:
            print("Please enter a number that is more than zero.")

# Main Routine starts here...
keep_going = ""
while keep_going == "":

    # Get width and height 
     width = num_check("width: ")
     height = num_check("height: ")

    # Calculate area / perimeter
     area = width * height 
     perimeter = 2 * (width + height)

    # Display output 
     print()
     print(f"Perimeter: {perimeter} units")
     print(f"Area: {area} square units")

    # Ask user if they want to keep going 
     keep_going = input("Press enter to keep going or any key to quit ")
     print()

print("Thank you for using the area / perimeter calculator")