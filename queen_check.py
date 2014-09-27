def CopyList(l):
    _l = []
    for i in range(0, len(l)):
        _l.append(l[i])
    return _l

def DecodePosition(s):
    pos = s[1:len(s)-1].split(",")
    pos[0] = int(pos[0])
    pos[1] = int(pos[1])
    return pos

def CheckPosition(pos):
    return pos[0]>0 and pos[0]<9 and pos[1]>0 and pos[1]<9

def PossibleKingMoves(pos):
    moves = []
    offs = [-1, 1, 0]
    for i in range(0, 3):
        for j in range(0, 3):
            if(offs[i]!=offs[j] or offs[i]!=0):
                p = [pos[0]+offs[i], pos[1]+offs[j]]
                if(CheckPosition(p)):
                    moves.append(p)
    return moves

def PossibleQueenMoves(pos):
    moves = []
    # horizontal moves
    for i in range(1, 9):
        if(i != pos[0]):
            #print("move [%d, %d]"%(i,pos[1]))
            moves.append([i, pos[1]])
    # vertical moves
    for i in range(1, 9):
        if(i != pos[1]):
            #print("move [%d, %d]"%(pos[1], i))
            moves.append([pos[0], i])
    # diagonal moves
    offs = [-1, 1]
    for i in range(0, 2):
        for j in range(0, 2):
            xoff = offs[i]
            yoff = offs[j]
            p = [pos[0]+xoff, pos[1]+yoff]
            while(CheckPosition(p)):
                #print("diagonal [%d, %d]" % (p[0],p[1]))
                moves.append(CopyList(p))
                p[0] += xoff
                p[1] += yoff
    return moves

def QueenCheck(strArr):
    queen_pos = DecodePosition(strArr[0])
    king_pos = DecodePosition(strArr[1])
    queen_moves = PossibleQueenMoves(queen_pos)
    king_moves = PossibleKingMoves(king_pos)
    is_check = queen_moves.count(king_pos)>0
    result = -1
    if(is_check):
        moves = []
        for i in range(0, len(king_moves)):
            if(queen_moves.count(king_moves[i])==0 or king_moves[i]==queen_pos):
                moves.append(CopyList(king_moves[i]))
        result = len(moves)
    return result
  
print QueenCheck(raw_input())
