# Note: We will practice writing simple functions in this exercise to get
# the muscle memory in our fingers going (with typing python functions).

# Question 1: You can define a function using the 'def' keyword. Create
# a function called say_hello which does not take any arguments as parameters
# and simply prints "Hello" within the function. If this function were called
# it would print "Hello" to the screen. Note: No explicit return values.
## Write your code below
def say_hello():
    print("Hello")

# End question 1

# Question 2: Create a new function called say_hello_premium(). This will return
# the string "Hello" to the caller. Note: No print required.
## Write your code below
def say_hello_premium():
    return("Hello")

# End question 2

# Question 3: Create a new function called yell_message() which takes a string
# as an argument. Example def yell_message(some_string). This function takes
# the parameter some_string, and prints it out to the screen after using the
# upper method on it to capitalize all the letters in the string. Example, if
# you called the function like this: yell_message("lol"), the output to the
# screen would be LOL.
## Write your code below
def yell_message(name):
    print(name.upper())


# End question 3
