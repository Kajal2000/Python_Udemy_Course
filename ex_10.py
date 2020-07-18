# Note: We will practice writing some more simple functions in this exercise

# Question 1: Write a function called simple_mult. It takes 2 arguments
# as parameters and returns their multiplied value. Assume only numbers are
# passed in as arguments, so you don't have to test for if the parameters
# are numbers are not.
## Write your code below
def simple_mult(num1,num2):
    num = num1 * num2
    return num
# End question 1

# Question 2: Create a new function called simple_mult_premium(). This will
# take two numbers as parameters (int or float). You will need to check for if
# both the parameters passed in are either of type "int" or "float" and return
# their multiplied value if they are. If either of them are not "int" or "float"
# return the string "Need either int or float". You can use the isinstance
# function to test the type of the parameter. Example if you were testing num_1,
# you can use code like isinstance(num_1, (int, float)) to test for int or float.
# This expression will return True if num_1 is of type int or float (passed in
# as a tuple here). You can also do this individually like below
# isinstance(num_1, int)
## Write your code below
def simple_mult_premium(num1 , num2):
    check_num1 = isinstance(num1 , int)
    check_num2 = isinstance(num2 , float)
    if check_num1 == True or check_num2==True:
        return(num1*num2)
    elif check_num2 == True or check_num1==True:
        return(num1*num2)
    else:
        return("Need either int or float")

# End question 2

# Question 3: Create a new function called create_divider() which takes a string
# as an argument and multiplies it by 40 to create a line full of the string
# and prints it out to the screen. Example "-" * 10 would give you
# ---------- so you can then use this function later on to create dividers in
# your output if you wanted. Remember to multiply by 40 and not 10.
## Write your code below
def create_divider(str):
    print(str*40)
# End question 3
