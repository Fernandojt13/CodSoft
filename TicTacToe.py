import random
theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}
board_keys = list(theBoard.keys())
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
def checkWin(board, mark):
    return ((board['7'] == board['8'] == board['9'] == mark) or
            (board['4'] == board['5'] == board['6'] == mark) or
            (board['1'] == board['2'] == board['3'] == mark) or
            (board['1'] == board['4'] == board['7'] == mark) or
            (board['2'] == board['5'] == board['8'] == mark) or
            (board['3'] == board['6'] == board['9'] == mark) or
            (board['7'] == board['5'] == board['3'] == mark) or
            (board['1'] == board['5'] == board['9'] == mark))
def checkTie(board):
    for key in board_keys:
        if board[key] == ' ':
            return False
    return True
def minimax(board, depth, isMaximizing):
    if checkWin(board, 'O'):
        return 1
    if checkWin(board, 'X'):
        return -1
    if checkTie(board):
        return 0
    if isMaximizing:
        bestScore = -float('inf')
        for key in board_keys:
            if board[key] == ' ':
                board[key] = 'O'
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = float('inf')
        for key in board_keys:
            if board[key] == ' ':
                board[key] = 'X'
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                bestScore = min(score, bestScore)
        return bestScore
def cpuMove():
    bestScore = -float('inf')
    bestMove = ''
    for key in board_keys:
        if theBoard[key] == ' ':
            theBoard[key] = 'O'
            score = minimax(theBoard, 0, False)
            theBoard[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    theBoard[bestMove] = 'O'
def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(theBoard)
        if turn == 'X':
            print("It's your turn, " + turn + ". Move to which place?")
            move = input()
            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            else:
                print("That place is already filled. Move to which place?")
                continue
        else:
            cpuMove()
            count += 1
        if count >= 5:
            if checkWin(theBoard, 'X'):
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** X won. ****")
                break
            elif checkWin(theBoard, 'O'):
                printBoard(theBoard)
                print("\nGame Over.\n")
                print("**** O won. ****")
                break
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")
            break
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    restart = input("Do you want to play again? (y/n)")
    if restart.lower() == 'y':
        for key in board_keys:
            theBoard[key] = ' '
        game()
if __name__ == "__main__":
    game()