#!/usr/bin/python3
# Run this script using the following command:
# python3 gradient_descent.py
import json
with open('samples.json') as samples_file:
	samples = json.load(samples_file)


from statistics import mean
from math import sqrt
import random

def hw(x):
	return w1 * x + w0

def loss():
	raise NotImplementedError() # TODO: Compute variance here

w1, w0 = 0, 0 # TODO: Initialize weights here
learning_rate = 0 # TODO: Initialize learning rate here

iteration = 0
steps_per_iteration = 50
while False: # TODO: Check for convergence here
	iteration = iteration + steps_per_iteration
	print(f"Iteration {iteration}, loss = {loss()}")
	
	for i in range(0, steps_per_iteration):
		raise NotImplementedError() # TODO: Adjust weights here

print(f"(w0, w1) = {(w0, w1)}")
print("Samples:")
for sample in samples:
	print((sample[0], sample[1], hw(sample[0])))
