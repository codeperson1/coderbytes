# What should this return when there are multiple patterns of the same length?
# Maybe try returning from most occurred to least occurred?
def PatternChaser(str):
    result = None
    length = len(str)
    while(length>1 and result==None):
        pos = len(str)-length
        while(pos > 0):
            pattern = str[pos:pos+length]
            if(str.count(pattern) > 1):
                result = pattern

                # if there are multiple patterns with the same length, then
                # 1 will return the last pattern in the string
                # 0 will return the first pattern in the string
                if(0):
                    break
            pos -= 1
        length -= 1
    if(result):
        result_str = "yes %s" % (result)
    else:
        result_str = "no null"
    return result_str

# keep this function call here  
# to see how to enter arguments in Python scroll down
#print PatternChaser(raw_input())  

#print(PatternChaser("da2kr32a2"))
#print(PatternChaser("sskfssbbb9bbb"))
print(PatternChaser("aaabbbaaa12cccxxxccc"))
