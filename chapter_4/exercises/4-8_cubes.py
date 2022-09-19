# 4-8. Cubes 
## A number raised to the third power is called a cube. 
## For example, the cube of 2 is written as 2**3 
## Make a list of the first 10 cubes, 1 through 10
## Use a for loop to print out the value of each cube 

cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
    print(cubes)