# 2021 Advent of Code
# Day 1

# Challenge 1 - count the number of times the depth increases when compared to the previous line
input_data = open("day1.txt", "r")
count = 0
last1 = 9999
last2 = 9999
currentsum = 0
prevsum = 999999


for line in input_data:
    if int(line) > last1:
        count = count + 1
    last1 = int(line)
print("Part 1: " + str(count))

# Challenge 2 - Compare the sum of the current value and past 2 values, how many increase now?
count = 0
for line in input_data:
    currentsum = int(line) + last1 + last2
    if currentsum > prevsum:
        count = count + 1
    prevsum = currentsum
    last2 = last1
    last1 = int(line)
    print(currentsum)
    print(prevsum)
    print(int(line))
    print(last1)
    print(last2)

print("Part 2: " + str(count))

input_data.close()