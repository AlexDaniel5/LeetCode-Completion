default: addTwoNumbers

addTwoNumbers.o: addTwoNumbers.c
	gcc -c addTwoNumbers.c -o addTwoNumbers.o
addTwoNumbers: addTwoNumbers.o
	gcc addTwoNumbers.o -o addTwoNumbers
clean:
	del addTwoNumbers.o
	del addTwoNumbers.exe