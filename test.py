#Add sorted lists and outputs to filess
'''outputFile1 = open("output.txt")
outputFile2 = open("outputRev.txt")
sortedFile1 = open("sorted.txt")
sortedFile2 = open("sortedRev.txt")'''

#compare normal sort
outputArray1 = []
for name in outputFile1:
	outputArray1.append(name.strip())
	
sortedArray1 = []
for name in sortedFile1:
	sortedArray1.append(name.strip())
	
if len(outputArray1) != len(sortedArray1):
	print("Forward sort failed")
else:
	sorted = bool(True)
	for i in range(0,len(outputArray1)):
		if outputArray1[i] != sortedArray1[i]:
			sorted = bool(False)
			break
	if sorted == True:
		print("Forward sort successful")
	else:
		print("Forward sort failed")
		
#compare reverse sort
outputArray2 = []
for name in outputFile2:
	outputArray2.append(name.strip())
	
sortedArray2 = []
for name in sortedFile2:
	sortedArray2.append(name.strip())
	
if len(outputArray2) != len(sortedArray2):
	print("Reverse sort failed")
else:
	sorted = bool(True)
	for i in range(0,len(outputArray2)):
		if outputArray2[i] != sortedArray2[i]:
			sorted = bool(False)
			break
	if sorted == True:
		print("Reverse sort successful")
	else:
		print("Reverse sort failed")		