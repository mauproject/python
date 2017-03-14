# Write a Python program to accept a filename from the user and print the extension of that.

filename = input("Enter a fileName (xxx.ccc): ")

print (filename.split(".")[1])