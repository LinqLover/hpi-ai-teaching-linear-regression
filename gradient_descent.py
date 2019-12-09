#!/usr/bin/python3
# Run this script using the following command:
# python3 gradient_descent.py
import json
with open('samples.json') as samples_file:
	samples = json.load(samples_file)


from statistics import mean
import math
import random

def hw(x):
	return w1 * x + w0

def loss(samples, w1, w0):
	return math.sqrt(mean([(y - (hw(x))) ** 2 for [x, y] in samples]))

# TODO: Compute gradient here
def gradient_w0(samples, w1, w0):
	raise NotImplementedError()
def gradient_w1(samples, w1, w0):
	raise NotImplementedError()

w1, w0 = 0, 0 # TODO: Initialize weights here
learning_rate = 0 # TODO: Initialize learning rate here

iteration = 0
g0 = g1 = math.inf
while False: # TODO: Check for convergence here
	iteration += 1
	print(f"Iteration {iteration}: w = ({w0:.2f}, {w1:.2f}), loss = {loss(samples, w1, w0):.2f}, g = ({g0:.2f}, {g1:.2f})")
	
	# TODO: Update weights from gradient here
	pass

print("Samples:")
print("x, y, hw(x)")
for sample in samples:
	print(f"{sample[0]}, {sample[1]}, {hw(sample[0]):.2f}")
