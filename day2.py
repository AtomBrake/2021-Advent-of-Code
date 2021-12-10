# 2021 Advent of Code
# Day 2
# Challenge 1

import numpy

horizontal = 0
depth = 0

input_data = numpy.loadtxt("day2.txt", dtype="str", delimiter=" ")

for line in input_data:
            print(line[0])
            print(line[1])
            print(int(line[1]))
            if line[0] == "forward":
                horizontal = horizontal + int(line[1])
            if line[0] == "down":
                depth = depth + int(line[1])
            if line[0] == "up":
                depth = depth - int(line[1])

print("Depth: " + str(depth))
print("Horizontal: " + str(horizontal))
print("Product: " + str(depth * horizontal))



