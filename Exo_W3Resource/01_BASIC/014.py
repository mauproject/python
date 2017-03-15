# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

import calendar

a = calendar.Calendar("%i%i%i"%(2014, 7, 2))
b = calendar.Calendar("%i%i%i"%(2014, 7, 11))

b-a