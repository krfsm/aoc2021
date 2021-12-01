#!/usr/bin/env python3

total_measurements = 0

with open('input-1.txt', 'r') as f:
    inputs = [int(x) for x in f.read().splitlines()]

for i in range(1, len(inputs)):
    if inputs[i] > inputs[i-1]:
        total_measurements = total_measurements+1

print('increases:', total_measurements)
