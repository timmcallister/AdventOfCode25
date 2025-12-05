with open('data.txt') as f:
    board = f.readlines()
    x_len = len(board[0])
    y_len = len(board)

def on_board(pos):
    x, y = pos[0], pos[1]
    if x > x_len or x < 0:
        return False
    if y > y_len or y < 0:
        return False
    return True

def is_roll(pos):
    x, y = pos[0], pos[1]
    if board[x][y] == '@':
        return 1
    else:
        return 0

def rolls():
    sum = 0

    for x in range(x_len - 1):
        for y in range(y_len - 1):

            adj = 0

            if is_roll((x, y)) == 0:
                pass

            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    if i == 0 and j == 0:
                        pass
                    else:
                        if on_board((x+i, y+j)):
                            adj += is_roll((x,y))

            if adj < 4:
                sum += 1

    return sum

print(rolls())

# 6634 too high
# 6334 not