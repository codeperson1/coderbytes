_LOOKUP = "abcdefghijklmnopqrstuvwxyz"

# broken for some cases .... don't feel like fixing
def Encode(s):
    es = ''
    for i in range(0, len(s)-1):
        c1 = _LOOKUP.index(s[i])
        c2 = _LOOKUP.index(s[i+1])
        diff = abs(c1-c2)
        inc = 1 - 2*(c1>c2)
        start = c1
        stop = c2
        if(diff > 1):
            start += inc
            stop -= inc
        c = start
        while((stop-c)*(c-start) >= 0):
            es += _LOOKUP[c]
            c += inc
        if(diff == 0):
            es += 'N'
        elif(diff == 1):
            es += 'S'
        elif(diff == 2):
            if(c1 < c2):
                es += 'R'
            else:
                es += 'L'
        if(0):
            print("i = %d" % (i))
            print("s[i] = %s" % (s[i]))
            print("s[i+1] = %s" % (s[i+1]))
            print("c1 = %d" % (c1))
            print("c2 = %d" % (c2))
            print("start = %d" % (start))
            print("stop = %d" % (stop))
            print("diff = %d"%(diff))
            print("inc = %d" % (inc))
            print("")
    return es

def ReverseString(s):
    _s = ''
    i = len(s)-1
    while(i >= 0):
        _s += s[i]
        i -= 1
    return _s

def MatchSequence(s, start=0):
    length = -1
    last_c = _LOOKUP.index(s[start])
    if(last_c != -1):
        length = 1
        stop = False
        while(length<len(s)-start and not stop):
            if(_LOOKUP.count(s[start+length]) == 0):
                stop = True
            else:
                c = _LOOKUP.index(s[start+length])
                if(abs(c-last_c)!=1):
                    stop = True
                else:
                    last_c = c
                    length += 1    
    return length

def NextChunk(s, i):
    if(s[i] == 'N' or s[i] == 'L' or s[i] == 'R'):
        return i + 2
    if(s[i] == 'S'):
        return i + 3
    return i + MatchSequence(s, i)

def Decode(s):
    result = ''
    s = ReverseString(s)
    i = 0
    while(i < len(s)):
        is_last = (NextChunk(s, i)==len(s))
        if(s[i] == 'N'):
            result += s[i+1]
        elif(s[i] == 'L'):
            c = _LOOKUP.index(s[i+1])
            result += _LOOKUP[c-1]
            if(is_last):
                result += _LOOKUP[c+1]
        elif(s[i] == 'R'):
            c = _LOOKUP.index(s[i+1])
            result += _LOOKUP[c+1]
            if(is_last):
                result += _LOOKUP[c-1]
        elif(s[i] == 'S'):
            c1 = _LOOKUP.index(s[i+1])
            c2 = _LOOKUP.index(s[i+2])
            result += _LOOKUP[c1]
            if(is_last):
                result += _LOOKUP[c2]
        else:
            length = MatchSequence(s, i)
            c1 = _LOOKUP.index(s[i])
            c2 = _LOOKUP.index(s[i+length-1])
            inc = 1 - 2*(c1<c2)
            ch1 = _LOOKUP[c1+inc]
            ch2 = _LOOKUP[c2-inc]
            result += ch1
            if(is_last):
                result += ch2
            else:
                # this is needed for two special cases:
                # 1) "efghfghi"
                # 2) "abcddefg"
                if(_LOOKUP.count(s[i+length]) != 0):
                    c3 = _LOOKUP.index(s[i+length])
                    inc2 = 1 - 2*(c2<c3)
                    if(inc*inc2 < 0):
                        if(c2 != _LOOKUP.index(s[i+length])):
                            result += _LOOKUP[c2-inc]
        i = NextChunk(s, i)
    result = ReverseString(result)
    return result

def AlphabetRunEncryption(str): 
    return Decode(str)    
print(Decode("cdefghijklmnopqrstuvwxxwvusrqponmlkjihgf"))
# keep this function call here  
# to see how to enter arguments in Python scroll down
#print AlphabetRunEncryption(raw_input())
