# Question 1: Given the list below, print the min value from the list using the
# min function
my_list = [903,373,223,4031,2033,535,677,601,403,340,370,352,441,293,567,8888,1031,788,161]
## Write your code below, 1 line
print(min(my_list)) 
# End question 1

# Question 2: Given the list below, using the 'in' operator, print (True or False) if
# 'urgent' exists in the list.
my_words_list = ['extreme', 'arrow', 'urgently', 'important', 'Urgent', 'imperative']
## Write your code below, 1 line
print ("urgent" in my_words_list) 

# End question 2

# Question 3: Use the sorted function to sort my_list from question 1 and assign it to a variable
# named my_sorted_list
## Write your code below, 1 line
my_sorted_list =  my_list
my_sorted_list = sorted(my_sorted_list)
# print(my_sorted_list)


# End question 3

# Question 4: Use the sort method to sort my_list from above and print out my_list below it
## Write your code below, 2 lines
my_list.sort()
print(my_list)
# End question 4

# Question 5: Use the equality test to check if my_sorted_list is equal to my_list. Remember
# to print the result.
## Write your code below, 1 line
print(my_sorted_list == my_list)

# End question 5
