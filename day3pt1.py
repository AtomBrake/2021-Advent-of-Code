# 2021 Advent of Code
# Day 3
# Part 1

input_data = open("day3.txt", "r")
input_data2 = open("day3.txt", "r")
# print(input_data.readlines())

# # Test
# count = list(str(123456789))
# print(count[1])
# count[1] = 3
# print(count)

char1 = 0
char2 = 0
char3 = 0
char4 = 0
char5 = 0
char6 = 0
char7 = 0
char8 = 0
char9 = 0
char10 = 0
char11 = 0
char12 = 0

lines = 0

for line in input_data:
    lines = lines + 1
    if line[0] == "1":
        char1 = char1 + 1
    if line[1] == "1":
        char2 = char2 + 1
    if line[2] == "1":
        char3 = char3 + 1
    if line[3] == "1":
        char4 = char4 + 1
    if line[4] == "1":
        char5 = char5 + 1
    if line[5] == "1":
        char6 = char6 + 1
    if line[6] == "1":
        char7 = char7 + 1
    if line[7] == "1":
        char8 = char8 + 1
    if line[8] == "1":
        char9 = char9 + 1
    if line[9] == "1":
        char10 = char10 + 1
    if line[10] == "1":
        char11 = char11 + 1
    if line[11] == "1":
        char12 = char12 + 1

print(char1)
print(char2)
print(char3)
print(char4)
print(char5)
print(char6)
print(char7)
print(char8)
print(char9)
print(char10)
print(char11)
print(char12)

if char1 >= lines/2:
    char1 = "1"
else: char1 = "0"
if char2 >= lines / 2:
    char2 = "1"
else: char2 = "0"
if char3 >= lines / 2:
    char3 = "1"
else: char3 = "0"
if char4 >= lines / 2:
    char4 = "1"
else: char4 = "0"
if char5 >= lines / 2:
    char5 = "1"
else: char5 = "0"
if char6 >= lines / 2:
    char6 = "1"
else: char6 = "0"
if char7 >= lines / 2:
    char7 = "1"
else: char7 = "0"
if char8 >= lines / 2:
    char8 = "1"
else: char8 = "0"
if char9 >= lines / 2:
    char9 = "1"
else: char9 = "0"
if char10 >= lines / 2:
    char10 = "1"
else: char10 = "0"
if char11 >= lines / 2:
    char11 = "1"
else: char11 = "0"
if char12 >= lines / 2:
    char12 = "1"
else: char12 = "0"

print("Char1: " + str(char1))
print("Char2: " + str(char2))
print("Char3: " + str(char3))
print("Char4: " + str(char4))
print("Char5: " + str(char5))
print("Char6: " + str(char6))
print("Char7: " + str(char7))
print("Char8: " + str(char8))
print("Char9: " + str(char9))
print("Char10: " + str(char10))
print("Char11: " + str(char11))
print("Char12: " + str(char12))

binresult = str(char1) + str(char2) + str(char3) + str(char4) + str(char5) + str(char6) + str(char7) + str(char8) + str(char9) + str(char10) + str(char11) + str(char12)

print(binresult)
gamma = int(binresult, 2)

print("Gamma: " + str(gamma))

char1 = 0
char2 = 0
char3 = 0
char4 = 0
char5 = 0
char6 = 0
char7 = 0
char8 = 0
char9 = 0
char10 = 0
char11 = 0
char12 = 0

lines = 0
line = 0

for line2 in input_data2:
    lines = lines + 1
    if line2[0] == "1":
        char1 = char1 + 1
    if line2[1] == "1":
        char2 = char2 + 1
    if line2[2] == "1":
        char3 = char3 + 1
    if line2[3] == "1":
        char4 = char4 + 1
    if line2[4] == "1":
        char5 = char5 + 1
    if line2[5] == "1":
        char6 = char6 + 1
    if line2[6] == "1":
        char7 = char7 + 1
    if line2[7] == "1":
        char8 = char8 + 1
    if line2[8] == "1":
        char9 = char9 + 1
    if line2[9] == "1":
        char10 = char10 + 1
    if line2[10] == "1":
        char11 = char11 + 1
    if line2[11] == "1":
        char12 = char12 + 1

print(char1)
print(char2)
print(char3)
print(char4)
print(char5)
print(char6)
print(char7)
print(char8)
print(char9)
print(char10)
print(char11)
print(char12)

print("Lines: " + str(lines))

if char1 <= lines/2:
    char1 = "1"
else: char1 = "0"
if char2 <= lines / 2:
    char2 = "1"
else: char2 = "0"
if char3 <= lines / 2:
    char3 = "1"
else: char3 = "0"
if char4 <= lines / 2:
    char4 = "1"
else: char4 = "0"
if char5 <= lines / 2:
    char5 = "1"
else: char5 = "0"
if char6 <= lines / 2:
    char6 = "1"
else: char6 = "0"
if char7 <= lines / 2:
    char7 = "1"
else: char7 = "0"
if char8 <= lines / 2:
    char8 = "1"
else: char8 = "0"
if char9 <= lines / 2:
    char9 = "1"
else: char9 = "0"
if char10 <= lines / 2:
    char10 = "1"
else: char10 = "0"
if char11 <= lines / 2:
    char11 = "1"
else: char11 = "0"
if char12 <= lines / 2:
    char12 = "1"
else: char12 = "0"

print("Char1: " + str(char1))
print("Char2: " + str(char2))
print("Char3: " + str(char3))
print("Char4: " + str(char4))
print("Char5: " + str(char5))
print("Char6: " + str(char6))
print("Char7: " + str(char7))
print("Char8: " + str(char8))
print("Char9: " + str(char9))
print("Char10: " + str(char10))
print("Char11: " + str(char11))
print("Char12: " + str(char12))

binresult = str(char1) + str(char2) + str(char3) + str(char4) + str(char5) + str(char6) + str(char7) + str(char8) + str(char9) + str(char10) + str(char11) + str(char12)

epsilon = int(binresult, 2)

print("Epsilon: " + str(epsilon))

power = gamma * epsilon

print("Power: " + str(power))


input_data.close()