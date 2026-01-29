grid = {'red':[1, 2, 3],
        'blue':[3, 2, 1]}

result = ''
for color in grid:
    result += color + ': ' + str(grid[color]) + '\n'
print(result)
