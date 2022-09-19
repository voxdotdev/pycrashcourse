# writing over a tuple 

dimensions = (200, 50)
print("Original demensions:")
for dimension in dimensions:
    print(dimension)

# Associate a new tuple with the variable dimensions to overwrite list
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

