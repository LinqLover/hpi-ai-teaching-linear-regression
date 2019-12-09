CFLAGS=-I.
DEPS = samples.h
LIBS += -lm

gradient_descent: gradient_descent.c
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

gradient_descent_solution: gradient_descent_solution.c
	$(CC) -o $@ $^ $(CFLAGS) $(LIBS)

clean: 
	$(RM) *.o 
	$(RM) gradient_descent
