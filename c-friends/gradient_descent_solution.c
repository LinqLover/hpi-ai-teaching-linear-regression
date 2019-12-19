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
		sum += pow(hw(SAMPLES[i][0]) - SAMPLES[i][1], 2);
	}
	return sum;
}

double gradient_w0() {
	double sum = 0;
	for (int i = 0; i < SAMPLES_COUNT; i++) {
		sum += hw(SAMPLES[i][0]) - SAMPLES[i][1];
	}
	return learning_rate * sum;
}
double gradient_w1() {
	double sum = 0;
	for (int i = 0; i < SAMPLES_COUNT; i++) {
		sum += (hw(SAMPLES[i][0]) - SAMPLES[i][1]) * SAMPLES[i][0];
	}
	return learning_rate * sum;
}

void main() {
	srandom(time(NULL));
	w1 = ((double)rand() / RAND_MAX - 0.5) * 20, w0 = ((double)rand() / RAND_MAX - 0.5) * 200;
	learning_rate = 0.001;
	
	double g0 = INFINITY, g1 = INFINITY;
	for (int iteration = 0; pow(g0, 2) + pow(g1, 2) > 1e-6; iteration++) {
		printf("Iteration %i: w = (%.2f, %.2f), loss = %.2f, g = (%.2f, %.2f)\n", iteration, w0, w1, loss(w1, w0), g0, g1);
		
		g0 = gradient_w0(), g1 = gradient_w1();
		w0 -= g0, w1 -= g1;
	}
	
	printf("Samples:\n");
	printf("x, y, hw(x)\n");
	for (int i = 0; i < SAMPLES_COUNT; i++) {
		printf("%i, %i, %.2f\n", SAMPLES[i][0], SAMPLES[i][1], hw(SAMPLES[i][0]));
	}
}
