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

def gradient_w0(samples):
	return sum([hw(x) - y for [x, y] in samples])
def gradient_w1(samples):
	return sum([(hw(x) - y) * x for [x, y] in samples])

w1, w0 = random.uniform(-10, 10), random.uniform(-100, 100)
learning_rate = 0.001

iteration = 0
g0 = g1 = math.inf
while g0 ** 2 + g1 ** 2 > 1e-6:
	iteration += 1
	print(f"Iteration {iteration}: w = ({w0:.2f}, {w1:.2f}), loss = {loss(samples, w1, w0):.2f}, g = ({g0:.2f}, {g1:.2f})")
	
	g0, g1 = gradient_w0(samples), gradient_w1(samples)
	w0 -= learning_rate * g0
	w1 -= learning_rate * g1

print("Samples:")
print("x, y, hw(x)")
for sample in samples:
	print(f"{sample[0]}, {sample[1]}, {hw(sample[0]):.2f}")
# extra line for satisfaction of answer to everything
