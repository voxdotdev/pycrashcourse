# Overview of Chapter 8 - Functions

## Key Information 

### Basic Functions

  * The keyword **def** is know as a function definition, tells Python the name of the function and, if applicable, what kind of information the function needs.
  * Including a **""" """** comment in the body of the function is called a **docstring**, Python looks for this when generating documentation for functions in programs.
  * When you want to use a function, you *call it*, by writing its name followed by **( )** and any required information inside of the **( )**. 
  * If the function does not need any information, that is if all the variables is uses are defined inside of it, these **( )** will be empty.
  
### Passing information to Functions

  * By adding a variable to the parentheses of the function, the function now expects you to declare a value for that variable whenever you call it.
  * A **Parameter** is what gets passed **INTO** a function. In the greeter exercise, (**username**) was the parameter.
  * An **Argument** is what gets passed **FROM** a function call to a function. In the greeter exercise, (**jesse**) was the argument in the function call.

#### Passing Arguments 

* Python must match each argument in the function call with a parameter in the function definition. The easiest way to do this is based on the order of the arguments provided. Values provided this way are called *positional arguments*. Essentially, just pass the definitions in the order the function defines them in. Order Matters.

#### Multiple Function Calls
* A function can be called as many times as needed simply by calling the same function again with different definitions for keywords.

#### Keyword Arguments 

* A *keyword argument* is a name-value pair that gets passed to a function by directly associating the name and the value within the argument. When the argument is passed to the function, there's no confusion on the order. The order doesn't matter since you're specifying the variable the definition your supplying is intended for.

#### Default Values

* A *default value* can be defined for each parameter that will be used if an argument for a parameter is provided. If no value is defined through an argument for a parameter, the default value will be used.
* When using default values, they must be defined / listed in the **( )** parameter field after all other parameters that do not have defaults. This allows Python to continue interpreting positional arguments correctly.

#### Equivalent Function Calls

* Positional args, keyword args, and default values can all be used together, as such there will be times where there will be multiple ways to call a function. Use whatever is easiest to understand, and if ever there are argument errors, Python should point out the problematic one in the returned error.

### Return Values
* A function doesn't always have to display its output directly. Instead, it can process some data and then return a value or set of values. The value the function returns is called a *return value*. The return statement takes a value from inside a function and sends it back to the line that called the function. Return values allow to move much of the program's grunt work into functions. 
  
#### Making an Argument Optional

* Sometimes it makes sense to make an argument optional so that people using the function can choose to provide extra information only if they want to. 
* Arguments can be made optional via default values.

#### Returning a Dictionary

* A function can return any kind of value needed, including more complicated data structures like lists and dictionaries.