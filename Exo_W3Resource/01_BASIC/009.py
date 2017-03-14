# Write a Python program to display the examination schedule. (extract the date from exam_st_date).
# Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (11, 12, 2014)

# My Proposal
exam_date = str(exam_st_date[0]) + " / " + str(exam_st_date[1]) + " / " + str(exam_st_date[2])
print ("The examination will start from : " + exam_date)

# Another Proposal
print( "The examination will start from : %i / %i / %i"%exam_st_date)