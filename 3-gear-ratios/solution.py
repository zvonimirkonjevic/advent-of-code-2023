inputs, visited = [], set()
DIRECTIONS = [
    (-1,-1), #top-left
    (-1,0), #top
    (-1,1), #top-right
    (0,-1), #left
    (0,1), #right
    (1,-1), #bottom-left
    (1,0), #bottom
    (1,1) #bottom-right
]
def is_adjacent_to_symbol(row, col):
    for dx, dy in DIRECTIONS:
        if 0 <= row + dx < len(inputs) and 0 <= col + dy < len(inputs[row + dx]):
            if not(inputs[row + dx][col + dy].isdigit() or inputs[row + dx][col + dy]=='.'):
                return True
    return False

with open('input.txt', 'r') as f:
    for line in f.readlines():
        inputs.append(list(line.strip()))
total = 0
for i, row in enumerate(inputs):
    j = 0
    while j < len(row):
        if row[j].isdigit() and (i, j) not in visited:
            number, init_j = row[j], j
            while j + 1 < len(row) and row[j + 1].isdigit():
                number += row[j + 1]
                j += 1
            for col_index in range(init_j, j + 1):
                visited.add((i, col_index))
                if is_adjacent_to_symbol(i, col_index):
                    total += int(number)
                    break
        j += 1
print(total)
