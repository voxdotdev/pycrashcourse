# Overview of Chapter 5

## If Statements

* This chapter will review how to write conditional tests which identify any condition of interest. Writing simple to complex if statements will be explored, as well as how to apply them to lists and integrate conditionals in for loops.

### Equality Operator 

One equal sign assigns a variable a value.

> variable = 'item1'</br>
Two equal signs checks if a variable equals a value: </br>
> variable == 'item2' </br>
> False

### Ignoring Case When Checking for Equality 

* Testing for equality is case sensitive in Python. Two values with different capitalization are not considered equal. 

* In a situation where case doesn't matter and the goal is to just test a variable, the variable's value can be converted to lowercase before doing the comparison. 

> variable = 'Item'</br>
> variable.lower() == 'item'

* This can also be used to test if something is not equal</br>
> answer = 17</br>
> if answer != 42</br>

* As well as other mathematical comparisons using equality operators 
> answer < 21</br>
> answer <= 21</br>
> answer > 21</br>
> answer >= 21

* Each mathematical comparison can be used as part of an if statement which can help detect exact conditions of interest.


## Checking Multiple Conditions 

* AND operator, if all tests pass, the result is True
* OR operator, if at least one test passes, the result is True

See [More Conditions](../exercises/5-2_more_con_tests.py) exercise for examples

### Checking whether a Value is Not in a List

[Banned user list exercise](../exercises/2_banned_users.py)

### Boolean Expressions

* A Boolean expression is just another name for a conditional test. A Boolean value is either True or False, just like teh value of a conditional expression after it has been evaluated.

* Boolean values are often used to keep track of conditions, for example if a game is running, or whether a user can edit certain content on a website.

>game_active = True</br>
>can_edit = False


## if Statements 

* Many kinds of if statements exist and the choice depends on the number of conditions needed to test. 

### Simple if Statements

> if conditional_test:</br>
> > do something

* The do something will execute if conditional_test is true, otherwise it will be ignored.
* Indentation matters in if statements, like for loops in the previous chapter.

### if-else statements

* Same as simple, however if test fails the statement will default to the else definition and perform actions.

See [Voting](../exercises/3_voting.py) exercise for simple if and if-else examples.

### The if-elif-else Chain

* When testing more than two possible situations, or to evaluate these, Python's if-elif-else syntax can be used. Python executes only one block in an if-elif-else chain. It runs each conditional test in order until one passes. When a test passes, the code belonging to that block is executed.

* Real world example of use: Amusement park that charges different rates for different age groups
  * Admission is free for anyone under age 4 
  * Admission is $25 for anyone between ages 4 and 18
  * Admission is $40 for anyone age 18 or older

* You can use as many elif blocks in your code as you'd like. 

* Python also does not require an else block at the end of an if-elif chain. Sometimes an else block is useful; sometimes it is clearer to use an additional elif statement that catches the specific condition of interest. 

See [Amusement Park](../exercises/4_amusement_park.py) exercise for if-elif-else examples. 

### Testing Multiple Conditions 

The if-elif-else chain is generally on appropriate to use when you just need one test to pass. As soon as Python finds one test that passes, the rest are skipped. 

In a situation where multiple conditions need to be checked, a series of if statements with no elif or else blocks can be used. 

See [Toppings](../exercises/5-0_toppings.py) exercise for if-elif-else examples. 

* In summary, if only one block of code needs to run, use an if-elif-else chain. If more than one block of code needs to run, use a series of independent if statements.

## Using if Statements with Lists 

When combining lists and if statements, it becomes possible to do thing like watch for special values that need to be treated differently than other values in the list. It allows management of changing conditions efficiently, such as the availability of certain items ina  restaurant throughout a shift. It also beings to prove that the code works as expected in all possible situations. 

### Checking for special items 

This chapter began with a simple example that showed how to handle a special value like 'bmw', which needed to be printed in a different format than other values in the list. Now that there's a basic understanding of conditional tests and if statements, we can now take a closer look at how special values can be accounted for in a list, and how to handle them appropriately. 

Continuing with the pizzeria example, the pizzeria displays a message whenever a topping is added to a pizza, as it's being made. The code for this action can be written by making a list of toppings the customer has requested, then using a loop to announce each topping as it's added to the pizza. 

## Checking That a List IS Not Empty

Soon the programs made will rely on user input to form the lists, in which case it will no longer be safe to assume the lists are populated with values. An if statement before the for loop will help with this.

See [Toppings Two](../exercises/5-0_toppings2.py) exercise.

## Using Multiple Lists

Lists and if statements can be used to make sure the user input makes sense before acting on it. Essentially compare one list to another, a list with user input to a list with valid entries.

## Styling if Statements 

The only recommendation PEP 8 provides for styling conditional tests is to use a single space around comparison operators, such as ==. >=, <=. 
 
>if age < 4</br>
is better than:</br>
>if age<4

## Summary of Chapter 5 

* How to write conditional tests, which always evaluate to true or false.
* How to write simple if statements, if-else chains, if-elif-else chains. 
* Identify conditions with these statements
* Handle certain items in a list differently than all other items,
  while utilizing the efficiency of a for loop. 
* Revisited Python's style recommendations 

