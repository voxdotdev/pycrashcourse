#if-elif-else chain 

age = 4
tier1 = 0
tier2 = 25
tier3 = 40

if age < 4:
    print(f"Your admission cost is ${tier1}.")
elif age < 18:
    print(f"Your admission cost is ${tier2}.")
else:
    print(f"Your admission cost is ${tier3}.")


# alternate, more succinct way 

age = 65  

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")


# Example to show multiple elifs allowed 

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 35

print(f"Your admission cost is ${price}.")


# Example omitting the else block 

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age >= 65:
    price = 20