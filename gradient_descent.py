#!/usr/bin/python3
import json
with open('samples.json') as samples_file:
	samples = json.load(samples_file)

import math
import random

def hw(x):
	return w1 * x + w0

def loss(samples, w1, w0):
	return sum([(hw(x) - y) ** 2 for [x, y] in samples])

# TODO: Compute gradient here
def gradient_w0(samples):
	raise NotImplementedError()
def gradient_w1(samples):
	raise NotImplementedError()

w1, w0 = 0, 0 # TODO: Initialize weights here
learning_rate = 0.001

iteration = 0
g0 = g1 = math.inf
while False: # TODO: Check for convergence here
	iteration += 1
	print(f"Iteration {iteration}: w = ({w0:.2f}, {w1:.2f}), loss = {loss(samples, w1, w0):.2f}, g = ({g0:.2f}, {g1:.2f})")
	
	g0, g1 = gradient_w0(samples), gradient_w1(samples)
	# TODO: Update weights from gradient here
	pass

print("Samples:")
print("x, y, hw(x)")
for sample in samples:
	print(f"{sample[0]}, {sample[1]}, {hw(sample[0]):.2f}")
