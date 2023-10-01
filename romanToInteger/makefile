default: romanToInt

romanToInt.o: romanToInt.c
	gcc -c romanToInt.c -o romanToInt.o
romanToInt: romanToInt.o
	gcc romanToInt.o -o romanToInt
clean:
	del romanToInt.o
	del romanToInt.exe