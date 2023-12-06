import re
inputs = []
NUMBERS = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}
with open("input.txt", "r") as input:
    for line in input.readlines():
        inputs.append(line.replace("\n", ""))

def part_one_solution(inputs):
    numbers = []
    for input in inputs:
        numbers.append(re.sub(r'[^0-9]', '', input))
    sum = 0
    for number in numbers:
        if len(number) == 1:
            sum += int(number)*10 + int(number)
        elif len(number) > 2:
            sum += int(number[0])*10 + int(number[-1])
        else:
            sum += int(number)
    print(sum)

def part_two_solution(inputs):
    sum = 0
    for input in inputs:
        all_substrings, number = [], ""
        for i in range(len(input)):
            temp = ""
            for j in range(i, len(input)):
                temp += input[j]
                if temp in NUMBERS:
                    number += str(NUMBERS[temp])
                elif temp.isdigit() and len(temp) == 1:
                    number += temp
        if len(number) == 1:
            sum += int(number) * 10 + int(number)
        elif len(number) > 2:
            sum += int(number[0]) * 10 + int(number[-1])
        else:
            sum += int(number) if number != '' else 0
    print(sum)