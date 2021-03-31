#Test normal sort
python3 sort.py < sorted.txt > output.txt
if diff output.txt sorted.txt; then
	echo "Sort passed"
else
	echo "Sort failed"
fi

#Test reverse sort
python3 sort.py -r < sortedRev.txt > outputRev.txt
if diff outputRev.txt sortedRev.txt; then
	echo "Reverse sort passed"
else
	echo "Reverse sort failed"
fi