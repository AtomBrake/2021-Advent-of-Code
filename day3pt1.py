# 2021 Advent of Code
# Day 3
# Part 1

input_data = open("day3.txt", "r")
# print(input_data.readlines())

count = 000000000000
lines = 0
column = 0
for line in input_data:
    lines = lines + 1
    column = column + 1
    print(column)
    for col in line:
        print(col)
        if str(col) == "1":
            count = count + 1
    print(count)
    print(lines)


input_data.close()