def ClosingBracket(s):
    if(s == '('):
        return ')'
    if(s == '['):
        return ']'
    return None

def MultipleBrackets(str):
    brackets = []
    i = 0
    num_brackets = 0
    valid = True
    
    while(i < len(str) and valid):
        if(str[i] == '[' or str[i] == '('):
            brackets.append(str[i])
        elif(str[i] == ']' or str[i] == ')'):
            if(len(brackets) == 0):
                valid = False
            elif(str[i] != ClosingBracket(brackets[len(brackets)-1])):
                valid = False
            else:
                num_brackets += 1
                brackets = brackets[0:len(brackets)-1]
        i += 1
    if(len(brackets)!=0):
      valid = False

    #print("num_brackets = %d" % (num_brackets))
    
    if(not valid):
        result_str = '0'
    elif(num_brackets == 0):
        result_str = '1'
    else:
        result_str = '1 %d' % (num_brackets)

    return result_str
    
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print MultipleBrackets(raw_input())           
