# 3-10. every Function 
# Think of something you could store in a list.
# Write a program that uses every function introduced in this chapter.

jobs = ['Comp Scientists', 'Net Architects', 'Developer', 'Info Sec', 'Data Admins']

# Print list 
print(f"Some occupations in tech: {jobs}.")

# Print one item in list 
print(f"I'm working to become a {jobs[2]}.")

# Change an item in the list

jobs[0] = 'Computer Scientists'
print(f"{jobs}")

# add an item in the middle of the list

jobs.insert(0, 'Sys Analysts')
print(jobs)
# add an item to the end of the list

jobs.append('Programmers')
print(jobs)
# delete an item from the list 

del jobs[-1]
print(jobs)

# Remove and reuse via pop method
popped_job = jobs.pop()
print(jobs)
# Remove and reuse an item from the list 

stored_job = 'Sys Analysts'
jobs.remove(stored_job)
print(jobs)

# Temporarily sort the list alphabetically

print(sorted(jobs))

# Permanently sort the list reverse alphabetically 

jobs.sort(reverse=True)
print(jobs)

# Permanently sort the list alphabetically 

jobs.sort()
print(jobs)

# Find the length of the list 

print(len(jobs))