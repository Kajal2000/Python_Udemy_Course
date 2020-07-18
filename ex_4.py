# Question 1: Write an if/else condition to print "Access granted"
# if the account variable is equal to the string "verified" AND
# payment_status is "paid". Else print "Access denied".
account = "verified"
payment_status = "paid"
## Write your code below (variable number of lines)
if account == "verified" and payment_status == "paid":
    print("Access granted")
else:
    print("Access denied")


## End question 1

# Question 2: Modify your code above and introduce a check for
# if account == "verified" and payment_status == "pending", then
# print "Temporary access granted, check payment status", if the
# payment status does not match either "pending" or "paid" (and
# the account is still verified) then print "Access denied, check payment". 
# Other conditions from question 1 above still apply.
account = "verified"
payment_status = "pending"
## Write your code below (variable number of lines)
if account == "verified" and payment_status == "paid":
    print( "Temporary access granted, check payment status")
elif account == "verified" and payment_status == "pending":
    print( "Temporary access granted, check payment status")
else:
    print("Access denied, check payment")



## Copy/paste your code (entire block for question 2) below, this
# if for a separate test for payment_status
payment_status = "blocked"
if account == "verified" and payment_status == "paid":
    print( "Temporary access granted, check payment status")
elif account == "verified" and payment_status == "pending":
    print( "Temporary access granted, check payment status")
else:
    print("Access denied, check payment")


## End question 2

# Question 3: Write an if/elif/else condition to check for the 3 account
# types below and print the corresponding statement. If account type
# matches none of these then it should print "Access denied"
# a) account_type == "admin", should result in print "Admin access"
# b) account_type == "mod", should result in print "Moderator access"
# c) account_type == "user", should result in print "User access"
account_type = "user"
## Write your code below (variable number of lines)
if account_type == "admin":
    print("Admin access")
elif account_type == "mod":
    print("Moderator access")
elif  account_type == "user":
    print("User access")
else:
    print("Access denied")

## End question 3
