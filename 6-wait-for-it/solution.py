import re
inputs = []
with open("input.txt", "r") as input:
    for line in input.readlines():
        inputs.append(re.sub(r'^.*:', '', line).rstrip())

def part_one_solution(inputs):
    times, distances = inputs[0].split(), inputs[1].split()
    total_ways = 1
    for i in range(len(times)):
        different_ways, j = 0, 1
        while (j < int(times[i])):
            if (int(times[i])-j)*j > int(distances[i]):
                different_ways += 1
            j += 1
        total_ways *= different_ways if different_ways != 0 else 1
    print(total_ways)

def part_two_solution(inputs):
    race_time = int(''.join(inputs[0].split()))
    race_distance = int(''.join(inputs[1].split()))
    total_ways = 1
    different_ways, j = 0, 1
    while (j < int(race_time)):
        if (int(race_time)-j)*j > int(race_distance):
            different_ways += 1
        j += 1
    total_ways *= different_ways if different_ways != 0 else 1
    print(total_ways)
