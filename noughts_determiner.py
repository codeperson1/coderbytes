EMPTY = '-'
X = 'X'
O = 'O'

class TicTacToeBoard():
    def __init__(self):
        self.board = []
        for i in range(0, 3):
            self.board.append([0,0,0])

    def set(self, x, y, value):
        self.board[x][y] = value

    def checkWin(self):
        # horizontal
        for j in range(0, 3):
            if(self.board[0][j] == X or self.board[0][j] == O):
                if(self.board[0][j] == self.board[1][j] == self.board[2][j]):
                    return True
        # vertical
        for j in range(0, 3):
            if(self.board[j][0] == X or self.board[j][0] == O):
                if(self.board[j][0] == self.board[j][1] == self.board[j][2]):
                    return True
        # diagonals
        if(self.board[1][1] == X or self.board[1][1] == O):
            diagonals = [
                [[0,0],[2,2]],
                [[2,0],[0,2]]
                ]
            for i in range(0, 2):
                if(self.board[diagonals[i][0][0]][diagonals[i][0][1]] == self.board[diagonals[i][1][0]][diagonals[i][1][1]] == self.board[1][1]):
                    return True
        return False

    def _testWin(self, x, y):
        if(self.board[x][y] == EMPTY):
            self.board[x][y] = X
            win = self.checkWin()
            self.board[x][y] = O
            win = win or self.checkWin()
            self.board[x][y] = EMPTY
        else:
            win = False
        return win

    def findWin(self):
        """ only works if there is no win yet """
        for x in range(0, 3):
            for y in range(0, 3):
                if(self._testWin(x,y)):
                    return [x,y]
        return None   
                
    def __str__(self):
        s = ''
        for y in range(0, 3):
            for x in range(0, 3):
                val = self.board[x][y]
                if(val == X):
                    s += 'X'
                elif(val == O):
                    s += 'O'
                else:
                    s += ' '
                if(x < 2):
                    s += '|'
            s += '\n'
            if(y < 2):
                s += '------\n'
        return s
'''
board = TicTacToeBoard()
board.set(1,0,X)
#board.set(1,1,X)
board.set(1,2,X)
print(board)
print(board.checkWin())
print(board.findWin())
'''

def NoughtsDeterminer(strArr): 
    result = None
    board = TicTacToeBoard()
    x = 0
    y = 0
    for i in range(0, len(strArr)):
      if(strArr[i] == '<>'):
        y += 1
        x = 0
      else:
        board.set(x,y,strArr[i])
        x += 1
    pos = board.findWin()
    result = 4*pos[1] + pos[0]
    return result

    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print NoughtsDeterminer(raw_input())  
















  
