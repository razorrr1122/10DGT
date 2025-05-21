# Demonstrate how to use while loops
# Joy kim
# 9 May 2025
# Version 1

# While loops
keep_going = "" # The variable contains an empty string
'''while keep_going == "" :

    like_c0ffee = input("Do you like coffee?")
    
    if like_c0ffee == "yes":  
       print("That is great. I like coffee tool")
       keep_going = "finished" 

       if like_c0ffee == "no":
           print("You are missing out. Why don't you give it a try.")
           keep_going = "finished" '''

# Version 2. Making the program more pythonic.
keep_going = ""
while keep_going == "":
    # .lower converts the answer to lower case
    like_coffee = input("Do you like coffee?").lower()
    if like_coffee == "yes" or like_coffee == 'y' :
        print("That is great. I like coffee too!")

    elif like_coffee == "no" or like_coffee == "n":
        print("You are missing out!")

        like_tea = input("Do you like tea instead?").upper()

        if like_tea == "Yuh uh" or like_tea == "Yep":
           print("Good for you. Give coffee another try :)")
        elif like_tea == "Nuh uh" or like_tea == "Nope":
            print("I am sorry/ That is all I have for now.")

    else: 
        print(" I don't understand . Please anser with either Yes or No.")

keep_going = input("Press <enter> to continue or any other key to quit.")

 # Version 3: improve(home)

while True: 

    like_coffee = input("Do you like coffee? ").lower()

    if like_coffee == "yes" or like_coffee == "y":
        print("That is great. I like coffee too!")
    elif like_coffee == "no" or like_coffee == "n":
        print("You are missing out!")
        like_tea = input("Do you like tea instead? ").lower()
        if like_tea == "yuh uh" or like_tea == "yep":
            print("Good for you. Give coffee another try :)")
        elif like_tea == "nuh uh" or like_tea == "nope":
            print("I am sorry! That is all I have for now.")
        else:
            print("I didn't quite get that about tea.")
    else:
        print("I don't understand. Please answer with either Yes or No.")
        continue  
    keep_going = input("Press <enter> to try again with coffee, or any other key to quit: ")
    if keep_going != "":
        break  