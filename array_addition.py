def ArrayAddition(arr):
    # tmparr = arr.copy()
    tmparr = []
    for i in range(0, len(arr)):
        tmparr.append(arr[i])
    tmparr.sort(reverse=True)
    most = tmparr[0]
    
    for i in range(0, len(tmparr)-1):
        total = tmparr[i]
        j = i + 1
        while(j < len(tmparr)):
            total += tmparr[j]
            if(total == most):
                return True
            j += 1
            
        j = i + 1
        while(j < len(tmparr)):
            total -= tmparr[j]
            if(total == most):
                return True
            j += 1
    return False

# keep this function call here  
# to see how to enter arguments in Python scroll down
#print ArrayAddition(raw_input())
#print(ArrayAddition([3,5,-1,8,12]))
print(ArrayAddition([-6,1,2,3,5,7]))
#print(ArrayAddition([9,3,2,1,2]))
#print(ArrayAddition([9,3,-5,-9,18])
