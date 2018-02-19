# Imports Here
import os
# Directory Creation Location
os.chdir('/Users/lukerhys/Desktop/test')
# Directory Prefix Variable can be anything you want
prefix = "Batch_"
# Input string as interger  - converted to range
batch_num = int(input("How many batches are you importing?:  "))
# For loop to add the batch prefix and create the directories
for f in range(batch_num):
	fileName = prefix + str(f)
	if os.path.exists('/Users/lukerhys/Desktop/test/' + fileName):
		print("Err: File already exists. Please try again.")
	else:
		os.mkdir(fileName)
