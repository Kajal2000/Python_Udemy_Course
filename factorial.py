def factorial_recur(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recur(n-1)

z = 5 # expecting 120
print(factorial_recur(z))