import re
inputs = []
with open("input.txt", "r") as input:
    for line in input.readlines():
        inputs.append(re.sub(r'^.*: ', '', line).rstrip())
total_points = 0
total_scratchcards = [1]*200
for i,input in enumerate(inputs):
    winning_numbers, card_numbers = input.split('|')
    winning_numbers = winning_numbers.split(' ')
    card_numbers =  card_numbers.split(' ')
    for number in winning_numbers:
        if not(number.isdigit()):
            winning_numbers.remove(number)
    for number in card_numbers:
        if not(number.isdigit()):
            card_numbers.remove(number)
    count = 0
    for number in winning_numbers:
        if number in card_numbers:
            count += 1
    total_points += pow(2, count-1) if (count > 0) else 0
    for j in range(count):
        total_scratchcards[j + i + 1] = total_scratchcards[j + i + 1] + total_scratchcards[i]
print(total_points)
print(sum(total_scratchcards[:i + 1]))
