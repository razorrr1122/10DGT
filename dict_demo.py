my_dict = {
    "blue": "sky",
    "double": 2,
    "half": 8.5,
    "green": "grass",
    "yellow": "sun",
    "red": "apple"
}

your_num = int(input("Enter a number: "))
to_do = input("double or half? ").lower()

# look up value 
multiply = my_dict[to_do]

# do math!
answer = your_num * multiply
print(f"{your_num} x {multiply} = answer" )