'''
Write a function that stores info about a car in a dictionary. 

The function should always receive a manufacturer and model name. 

It should then accept an arbitrary number of keyword arguments. **kwargs

Call the function with the required info and two other name-value pairs,
such as a color or an optional feature. Your function should work for a call like this one: 

car = make_car('subaru', 'outback', color='blue', tow_package=True)

Print the dictionary that's returned to make sure all teh info was stored correctly.

'''

def car_info(make, model, **kwargs):
    kwargs['make'] = make
    kwargs['model'] = model
    return kwargs

car_details = car_info('ford', 'focus', color='blue', fog_lamps=True, tow_package =False)
print(car_details)