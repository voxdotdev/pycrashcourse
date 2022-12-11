# 4-4. One Million
## Make a list of the numbers from 1 to 1 million
## use a for loop to print the numbers 

millions = []
for value in range (1,1000001):
    millions.append(value)

# 4-5. Summing a million 
## Use min, max, and sum functions to ensure list is populated with 1mill

print(f"Min: {min(millions)}, Max: {max(millions)}, Sum: {sum(millions)}")