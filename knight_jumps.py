#
# It is undefined to enter a position less than 1 or greater than 8
#

def CheckSpace(pos, board_size):
    i = 0
    while(i < 2):
        if(pos[i]<1 or pos[i]>board_size[i]):
            return False
        i += 1
    return True

def CountKnightMoves(pos, board_size):
    possible_moves = [
        [pos[0]+2, pos[1]-1],
        [pos[0]+2, pos[1]+1],
        [pos[0]-2, pos[1]-1],
        [pos[0]-2, pos[1]+1],
        [pos[0]-1, pos[1]-2],
        [pos[0]-1, pos[1]+2],
        [pos[0]+1, pos[1]-2],
        [pos[0]+1, pos[1]+2]
        ]
    
    num_moves = 0
    index = 0
    while(index < len(possible_moves)):
        if(CheckSpace(possible_moves[index], board_size)):
            num_moves += 1
        index += 1

    return num_moves

def ParsePositionStr(s):
    pos = s[1:len(s)-1].split(" ")
    pos[0] = int(pos[0])
    pos[1] = int(pos[1])
    return pos

BOARD_SIZE = [8, 8]

def KnightJumps(str):
    pos = ParsePositionStr(str)
    num = CountKnightMoves(pos, BOARD_SIZE)
    return num

print KnightJumps(raw_input())
