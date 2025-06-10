def num_check(question):...



# Main Routine starts here...

keep_going = ""
while keep_going == "":
    # Get width and height 
   width = num_check("Enter width: ")
   height = num_check("Enter height: ")
   cost_m = num_check("Enter cost per metre: ")

    # Calculate perimeter and price for the fence
   Perimeter = 2 * (width + height)
   cost_m = Perimeter * cost_m 

    # Output perimeter and cost  
   print()
   print(f"Perimeter: {width} units")
   print(f"Price: ${cost_m:.2f}")
   
    # Ask user if they want to keep going
keep_going = input("<enter> to loop, any key to quit")
print()

print("Thank you for using the fence cost calculator")

    