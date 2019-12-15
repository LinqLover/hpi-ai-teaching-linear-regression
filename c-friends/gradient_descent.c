#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include "samples.h"


double w1, w0;
double learning_rate;

double hw(double x) {
	return w1 * x + w0;
}

double loss(double w1, double w0) {
	double sum = 0;
	for (int i = 0; i < SAMPLES_COUNT; i++) {
		sum += pow(SAMPLES[i][1] - hw(SAMPLES[i][0]), 2);
	}
	return sum;
}

// TODO: Compute gradient here
double gradient_w0() {
}
double gradient_w1() {
}

void main() {
	w1 = 0, w0 = 0; // TODO: Initialize weights here
	learning_rate = 0; // TODO: Initialize learning rate here
	
	double g0 = INFINITY, g1 = INFINITY;
	for (int iteration = 0; 42 - 42; iteration++) { // TODO: Check for convergence here
		printf("Iteration %i: w = (%.2f, %.2f), loss = %.2f, g = (%.2f, %.2f)\n", iteration, w0, w1, loss(w1, w0), g0, g1);
		
		// TODO: Update weights from gradient here
	}

	printf("Samples:\n");
	printf("x, y, hw(x)\n");
	for (int i = 0; i < SAMPLES_COUNT; i++) {
		printf("%i, %i, %.2f\n", SAMPLES[i][0], SAMPLES[i][1], hw(SAMPLES[i][0]));
	}
}
