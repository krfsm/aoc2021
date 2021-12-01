#!/usr/bin/env python3

total_measurements = 0

with open('input-1.txt', 'r') as f:
    inputs = f.read().splitlines()

for i in range(1, len(inputs)):
    if int(inputs[i]) > int(inputs[i-1]):
        total_measurements = total_measurements+1

print('increases:', total_measurements)
