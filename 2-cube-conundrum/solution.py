import re
inputs, total = [], 0
with open("input.txt", "r")as input:
    for line in input.readlines():
        inputs.append(re.sub('\s+','',line))
for input in inputs:
    game, results = input.split(':')
    game_id = int(re.sub(r'Game', '', game))
    reds = [eval(i) for i in re.findall(r'(\d+)red', results)]
    blues = [eval(i) for i in re.findall(r'(\d+)blue', results)]
    greens = [eval(i) for i in re.findall(r'(\d+)green', results)]
    if(max(reds)<=12 and max(greens)<=13 and max(blues)<= 14):
        total += game_id
print(total)
