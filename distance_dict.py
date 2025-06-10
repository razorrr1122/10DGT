distance_dict= {
    "mm": 1000,
    "cm": 100, 
    "m": 1,
    "km": .1
}

# Get amount and units (assume they are valid)
amount = float(input("Amount? "))
from_unit = input("From unit? ")
to_unit = input("To unit? ")

# Multiply to get to our standard value...
multiply_by = distance_dict[to_unit]
standard = amount * multiply_by

# Divine to get to our desired value
divided_by = distance_dict[from_unit]
answer = standard / divided_by 

print(f"There are {answer} {to_unit} in {amount} {from_unit} ")