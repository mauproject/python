# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference

import math


# My Proposal

n = int(input("Enter a number: "))

if n <= 17:
    print(17 - n)
else:
    print(2 * abs(n-17))

# Another solution

def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

print(difference(22))
print(difference(14))