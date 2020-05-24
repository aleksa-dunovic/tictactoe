def print_board(board):
    print('\n')
    for i in range(len(board)):
        print("|", end='')
        for j in range(len(board[i])):
            print("  {}  |".format(board[i][j]), end='')
        
        print('\n')    


def game():
    g = False
    p1 = input('Player 1 Name: ')
    p2 = input('Player 2 Name: ')
    p = [p1, p2]
    icon = ['x', 'o']
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    print_board(board)
    
    while g == False:       
        for i in range(len(p)):            
            if winner(board):
                break
            
            w = p[i]
            
            print ('{}\'s turn'.format(p[i]))
            r = int(input('which row would you like to place an {}: '.format(icon[i]))) - 1
            if not (type(r) == int and r < 3 and r >= 0):
                print('Input error: row must be between 1 and 3')
                return
         
            c = int(input('which column would you like to place an {}: '.format(icon[i]))) - 1
            if not (type(c) == int and c < 3 and c >= 0):
                print('Input error: column must be between 1 and 3')
                return
            
            if board[r][c] == "-":
                board[r][c] = icon[i]
                print("\n")
            else:
                print("Input error: spot taken")
                return
            
            print_board(board)
        
        g = winner(board)
    
    print('{} is the winner!'.format(w))
    return


def winner(board):

    for r in range(3):
        row = set()
        for c in range(3):
            row.add(board[r][c])
        if len(row) == 1 and ("x" in row or "o" in row):
            return True
    
    for c in range(3):
        column = set()
        for r in range(3):
            column.add(board[r][c])
        if len(column) == 1 and ("x" in column or "o" in column):
            return True
        
    diagonal = set()
    for r in range(3):
        for c in range(3):
            if r == c:
                diagonal.add(board[r][c])

    if len(diagonal) == 1 and ("x" in diagonal or "o" in diagonal):
        return True
      
    return False


game()
