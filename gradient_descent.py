#!/usr/bin/python3
# Run this script using the following command:
# python3 gradient_descent.py
import json
with open('features.json') as features_file:
	features = json.load(features_file)


from statistics import mean
from math import sqrt
import random

def hw(x):
	return w1 * x + w0

def stddev():
	raise NotImplementedError() # TODO: Implement loss function here

w1, w0 = 0, 0 # TODO: Initialize weights here
learning_rate = 0 # TODO: Initialize learning rate here

iteration = 0
steps_per_iteration = 50
while True: # TODO: Check for convergence here
	iteration = iteration + steps_per_iteration
	print(f"Iteration {iteration}, stddev = {stddev()}")
	
	for i in range(1, steps_per_iteration):
		raise NotImplementedError() # TODO: Adjust weights here

print(f"(w0, w1) = {(w0, w1)}")
print()
for feature in features:
	print((feature[0], feature[1], hw(feature[0])))
