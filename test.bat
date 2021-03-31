python.exe sort.py < sorted.txt > output.txt
python.exe sort.py -r < sortedRev.txt > outputRev.txt
fc output.txt sorted.txt 
fc outputRev.txt sortedRev.txt

pause