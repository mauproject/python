# Write a Python program to display the first and last colors from the following list.

color_list = ["Red","Green","White" ,"Black"]

# My Proposal
print("First : " + color_list[0] + " \nLast  : " + color_list[color_list.__len__() - 1])

# Another proposal
print( "%s %s"%(color_list[0],color_list[-1]))
