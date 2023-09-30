default: failureAttempt

failureAttempt.o: failureAttempt.c
	gcc -c failureAttempt.c -o failureAttempt.o
failureAttempt: failureAttempt.o
	gcc failureAttempt.o -o failureAttempt
clean:
	del failureAttempt.o
	del failureAttempt.exe