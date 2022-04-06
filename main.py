
res = []
n = 8
rows = n
cols = n
    
# find whether a given charecter in empty -> used to find 
def available(board, x, y):

    # NOTES:
    # left to right diagonal - l2rd
    # right to left diagonal - r2ld

    for i in board[x]:
        if i == 1:
            return False

    # capturing the columns
    for j in range(len(board)):
        if board[j][y] == 1:
            return False

    # finding the start of the diagonal from l2rd
    start = [x - min(x, y), y - min(x, y)]

    # finding the difference to idenetify the cells with the same difference 
    # to determine the squares which will be captured, in the l2rd.
    diff = x - y
    for i in range(start[0], rows):
        for j in range(start[1], cols):
            if i - j == diff:
                try:
                    if board[i][j] == 1:
                        return False
                except Exception:
                    pass

    
    # finding the start of r2ld by using the following algorithm
    start = [x, y]
    while start[0] != 0 and start[1] != 7:
        start[0] -= 1
        start[1] += 1

    # the start and end of r2ld squares pattern:
    # start - (i, j)
    # end   - (j, i)

    i = start[0]
    j = start[1]

    # looping until the i value equals the second coordiante value, i.e until 
    # start equals the reverse of end
    while i != start[1] + 1:
        # board[i][j][0] = captured_str
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True



def solve(board, col, n = 8):

    # base case:
    # if all the coloumns are have a queen, then we have a finished set.
    # so we can add it to the list of solutions.
    if col == n:
        v = []
        for i in board:
            for j in range(len(i)):
                if i[j] == 1:
                    v.append(j + 1)
        res.append(v)
        return True


    # recursive case:
    # backtrack each time we can't find a solution and 
    # brute force the way until we do. 
    solved = False
    for i in range(len(board)):

        # if the position is available we place a queen 
        # and continiue for the fnal solution, if final solutioin is 
        # not available we backtrack and place the queen in a new
        # possible/available position 
        if available(board, i, col):
            board[i][col] = 1
            solve(board, col + 1)
            board[i][col] = 0

    return solved
        

if __name__ == "__main__":
    res.clear()
    n = 8
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0, n)
    res.sort()

    config_file = open('configs.txt', 'a')

    for i in range(len(res)):
        chess_board = [[0 for _ in range(n)] for _ in range(n)]
        solution = res[i]
        for row in range(len(chess_board)):
            for col in range(len(board[0])):
                if col == solution[row] - 1:
                    chess_board[row][col] = 'x'
                else:
                    chess_board[row][col] = ' '

        config_file.write(f"configuration {i + 1}\n")
        for row in chess_board:
            config_file.write(str(row))
            config_file.write('\n')

        config_file.write('\n')
