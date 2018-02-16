import os
os.chdir('C:\Users\GC4C-0013\Desktop\New folder')
batches = []
for i in range(1):
	batches = raw_input("How many batches are you importing?: ")
	batchNames = "batch_" + batches
os.mkdir(batchNames)














"""
#batchType = raw_input("Are you importing Irons, Bags or a Batch?: ")
print "How many batches are you importing?"
batchCount = raw_input() #splits the input string on spaces
input_list = batchCount.split()
# process string elements in the list and make them integers
input_list = [int(a) for a in input_list]
# for each item in the list of items
for value in batchCount:


batchCount = []
for i in range(1):
	numOfBatches = raw_input("How many batches are you importing?: ")
	batchCount.append(numOfBatches)
break
	return batchCount

	 construct the filename; prefix or suffix optional
filename = 'batch_' + batchCount
	 open the file to be written
directory = open(filename, 'w')
	write the content in the file including the value being passed to each; %s indicates a string
directory.write('%s' % batchCount)


	# example using an iframe
	# fo.write('<iframe src="http://www.washingtonpost.com/wp-srv/special/politics/election-map-2012/homepage/embed-map.html?mapstate=%s" width="610" height="502" scrolling="no" frameborder="0"></iframe>' % state)

	close the file
"""
