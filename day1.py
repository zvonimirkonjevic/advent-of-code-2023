import re
inputs = []
numbers = []
with open("day1_inputs.txt", "r") as day1_inputs:
    lines = day1_inputs.readlines()
    for line in lines:
        inputs.append(line.replace("\n", ""))
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