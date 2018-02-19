# Imports Here
import os
# Directory Creation Location
os.chdir(input('Where would you like to create the directories?  '))
# Directory Prefix Variable can be anything you want
prefix = "Batch_"
# Input string as interger  - converted to range
batch_num = int(input("How many batches are you importing?:  "))
output = batch_num + 1
# For loop to add the batch prefix and create the directories
for f in range(1, output, 1):
	fileName = prefix + str(f)
	if os.path.exists('/Users/lukerhys/Desktop/test/' + fileName):
		print("Err: File already exists. Please try again.")
	else:
		os.mkdir(fileName)
