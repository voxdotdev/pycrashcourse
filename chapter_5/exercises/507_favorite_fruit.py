"""
5-7. Favorite Fruit:
Make a list of your favorite fruits, call it favorite_fruits
Write five if statements. Each should check whether a certain kind of fruit is in your list. 
If the fruit is in the list, the if block should print a statement, such as "You really like bananas!"

"""

# Like exercise 5-6, input has not been reviewed yet in book.

favorite_fruit = ['apples','bananas','kiwi','lemons','melon']
fruit = input("Guess what kind of fruit I like! ").lower()

if fruit in favorite_fruit:
    print(f"Yep, I love {fruit}!")
else:
    print("No sorry, not a favorite of mine.")