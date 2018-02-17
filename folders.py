# Imports Here
import os

# Directory Creation Location
os.chdir('/Users/lukerhys/Desktop/test')

# Container for input
batches = ('')
# Directory Prefix can be anything you want
prefix = "Batch_"

# For loop to prompt human input of directory names
for i in range(1):
	batches_num = input("Which batches are you importing?:  ")

# For loop to ad the batch prefix and create the directories
for f in batches_num.split():
	fileName = prefix + f
	os.mkdir(fileName)
