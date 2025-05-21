# planning the area / perimeter 
# Version 1

# ask the user for a number
while True: 
    width = float(input("Width: ")) 

# check that the number is more than zero
    if width > 0:
        break
    else: 
         print("Please enter a number that is more than zero\n")
         
error = "Please enter a number that is more than zero\n"
while True: 

    try:
        width = float (input("Width; "))

        if width > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)

