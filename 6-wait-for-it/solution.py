import re
inputs = []
with open("input.txt", "r") as input:
    for line in input.readlines():
        inputs.append(re.sub(r'^.*:', '', line).rstrip())
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
