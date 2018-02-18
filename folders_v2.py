# Imports Here
import os

# Directory Creation Location
os.chdir('/Users/lukerhys/Desktop/test')

# Variable for input
batch_num = ('')
# Directory Prefix Variable can be anything you want
prefix = "Batch_"

batches_num = input("Which batches are you importing?:  ")

# For loop to prompt human input of directory names
#for i in batches_num:


# For loop to add the batch prefix and create the directories
for f in batches_num.split():
	fileName = prefix + f
	if os.path.exists('/Users/lukerhys/Desktop/test/' + fileName):
		os.mkdir(fileName + " copy")
		#print("true")
	else:
		os.mkdir(fileName)
		#
		#print("false")
#for filename in myFiles:
#        print(os.path.join('C:\\Users\\asweigart', filename)
