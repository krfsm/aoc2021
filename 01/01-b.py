#!/usr/bin/env python3

total_increases = 0

with open('input-1.txt', 'r') as f:
    inputs = [int(x) for x in f.read().splitlines()]

for i in range(3, len(inputs)):
    sum = inputs[i] + inputs[i-1] + inputs[i-2]
    prevsum = inputs[i-1] + inputs[i-2] + inputs[i-3]
    if sum > prevsum:
        total_increases = total_increases + 1

print('increases:', total_increases)