# Imports Here
import os

# Directory Creation Location
os.chdir(raw_input("Where would you like to create the directories?: "))

# Directory Prefix Variable can be anything you want
prefix = raw_input("How would you like to prefix your directories?: ")

# Input string as interger  - converted to range
batch_num = int(input("How many batches are you importing?: "))
output = batch_num + 1

# Where would you like to start the batch count
start_point = int(input("How many batches do you have so far?: "))
	if start_point == 0:
		correct_start = start_point + 1
	else:
		None

# For loop to add the batch prefix and create the directories
for f in range(start_point, output, 1):
	fileName = prefix + "_" + str(f)
	if os.path.exists(fileName):
		print("Err: File already exists. Please try again.")
	else:
		os.mkdir(fileName)
