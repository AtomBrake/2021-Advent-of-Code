# 2021 Advent of Code
# Day 2
# Challenge 2

import numpy

horizontal = 0
depth = 0
aim = 0

input_data = numpy.loadtxt("day2.txt", dtype="str", delimiter=" ")

for line in input_data:
    print(depth)
    print(horizontal)
    print(aim)
    if line[0] == "forward":
        horizontal = horizontal + int(line[1])
        depth = depth + (aim * int(line[1]))
    if line[0] == "down":
        aim = aim + int(line[1])
    if line[0] == "up":
        aim = aim - int(line[1])

print("Depth: " + str(depth))
print("Horizontal: " + str(horizontal))
print("Product: " + str(depth * horizontal))

