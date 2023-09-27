default: mergeAlternately

mergeAlternately.o: mergeAlternately.c
	gcc -c mergeAlternately.c -o mergeAlternately.o
mergeAlternately: mergeAlternately.o
	gcc mergeAlternately.o -o mergeAlternately
clean:
	del mergeAlternately.o
	del mergeAlternately.exe