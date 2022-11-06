'''
Make a dictionary containing three major rives and the country each river runs through. 
One key-value pair might be 'yangtze': 'china'.

1) Use a loop to print a sentence about each river, such as The RIVER runs through COUNTRY.

2) Use a loop to print the name of each river included in the dictionary.

3) User a loop to print the name of each country included in the dictionary.

'''

rivers = {'yangtze': 'china', 'mississippi': 'united states', 'amazon': 'brazil'}

#1, #2, #3
for key, value in rivers.items():
    print(f"River: {key.title()}")
    print(f"Country: {value.title()}")
    print(f"\n The {key.title()} river runs through {value.title()}.\n")