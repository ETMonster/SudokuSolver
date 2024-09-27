puzzle = open('puzzle.txt', 'r').read().split('\n')
for i in range(len(puzzle)):
    puzzle[i] = puzzle[i].split(' ')
    for j in range(len(puzzle[i])):
        puzzle[i][j] = int(puzzle[i][j])

def possible_numbers(row, col, box):
    r = list(range(1, 10))
    
    for n in row + col + box:
        if n in r:
            r.remove(n)
    
    return r

while any(n == 0 for row in puzzle for n in row):
    for (i, row) in enumerate(puzzle):
        for (j, num) in enumerate(row):
            if num != 0:
                continue

            col = [puzzle[k][j] for k in range(len(puzzle))]
            box = [puzzle[k][l] for k in range(i - (i % 3), i - (i % 3) + 3) for l in range(j - (j % 3), j - (j % 3) + 3)]

            result = possible_numbers(row, col, box)
            if len(result) == 1:
                puzzle[i][j] = result[0]

print('Solved sudoku:')
for x in puzzle:
    for n in x:
        print(f'{n} ', end = '')
    print('')