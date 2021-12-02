#!/usr/bin/env python3

with open('input-2.txt', 'r') as f:
    inputs = [x for x in f.read().splitlines()]

def part1():
    horizontal = 0
    vertical = 0
    for i in range(0, len(inputs)):
        word = inputs[i].split()[0]
        number = int(inputs[i].split()[1])
        if word == 'forward':
            horizontal = horizontal + number
        elif word == 'down':
            vertical = vertical + number
        elif word == 'up':
            vertical = vertical - number
    print('total mult', horizontal * vertical)

def part2():
    horizontal = 0
    vertical = 0
    aim = 0
    for i in range(0, len(inputs)):
        word = inputs[i].split()[0]
        number = int(inputs[i].split()[1])
        if word == 'down':
            aim = aim + number
        elif word == 'up':
            aim = aim - number
        elif word == 'forward':
            horizontal = horizontal + number
            vertical = vertical + (aim * number)
    print('total mult', horizontal * vertical)

part1()
part2()