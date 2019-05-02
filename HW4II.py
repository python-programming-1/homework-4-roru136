grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
heart = ''

for i in range(len(grid)):
    heart += str(grid[i][0])

heart1 = '\n'
for i in range(len(grid)):
    heart1 += str(grid[i][1])

heart2 = '\n'
for i in range(len(grid)):
    heart2 += str(grid[i][2])

heart3 = '\n'
for i in range(len(grid)):
    heart3 += str(grid[i][3])

heart4 = '\n'
for i in range(len(grid)):
    heart4 += str(grid[i][4])

heart5 = '\n'
for i in range(len(grid)):
    heart5 += str(grid[i][5])

print(heart+heart1+heart2+heart3+heart4+heart5)
