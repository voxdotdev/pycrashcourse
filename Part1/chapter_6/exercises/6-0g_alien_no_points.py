''' 
Using get() to Access Values 
The get method can be used to set a default value that will be returned if the requested key does not exist. 
If the key does exist the value will be returned, else the default message assigned to the key will be displayed.
If there's a chance the key you're asking for might not exist yet, consider using the get() method over square bracket notation.

'''
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No points value assigned.')
print(point_value)