# Imports Here
import os

# Directory Creation Location
os.chdir(input('Where would you like to create the directories?: '))

# Directory Prefix Variable can be anything you want
prefix = input("How would you like to prefix your directories?: ")

# Input string as interger  - converted to range
batch_num = int(input("How many batches are you importing?: "))
output = batch_num + 1

# Where would you like to start the batch count
start_point = int(input("How many batches do you have so far?: "))
start_num =start_point + output

# For loop to add the batch prefix and create the directories
for f in range(1, start_num, 1):
	fileName = prefix + "_" + str(f)
	if os.path.exists(fileName):
		print("Err: File already exists. Please try again.")
	else:
		os.mkdir(fileName)
