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
total_parts = 0
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
                    total_parts += int(number)
                    break
        j += 1
total_gear_ratios = 0
for i,row in enumerate(inputs):
    for j, char in enumerate(row):
        if char == '*':
            adjecent_numbers = []
            for dx, dy in DIRECTIONS:
                adjecent_row, adjecent_col = i + dx, j + dy
                if 0 <= adjecent_row < len(inputs) and 0 <= adjecent_col < len(inputs[adjecent_row]):
                    if inputs[adjecent_row][adjecent_col].isdigit():
                        number_str = inputs[adjecent_row][adjecent_col]
                        left_col = adjecent_col - 1
                        while left_col >= 0 and inputs[adjecent_row][left_col].isdigit():
                            number_str = inputs[adjecent_row][left_col] + number_str
                            left_col -= 1

                        right_col = adjecent_col + 1
                        while right_col < len(inputs[adjecent_row]) and inputs[adjecent_row][right_col].isdigit():
                            number_str = number_str + inputs[adjecent_row][right_col]
                            right_col += 1
                        part_number = int(number_str)
                        if part_number not in adjecent_numbers:
                            adjecent_numbers.append(part_number)
            if len(adjecent_numbers) == 2:
                total_gear_ratios += adjecent_numbers[0] * adjecent_numbers[1]

print(total_parts)
print(total_gear_ratios)
