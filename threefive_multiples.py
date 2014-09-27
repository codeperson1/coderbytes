def ThreeFiveMultiples(num):
    result = 0
    for i in range(1, num):
        n = num - i
        if((n%3 == 0) or (n%5 == 0)):
            result += n
    return result
    
# keep this function call here  
# to see how to enter arguments in Python scroll down
print ThreeFiveMultiples(raw_input())
