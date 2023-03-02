list1 = [3,5,7,2,4,61]

result = []
result.append(list1[0])

def maxNumber(list1):

    for i in range(1,len(list1)):

        if list1[i]> result[0]:
            result[0]=list1[i]
    
    return result[0]

print(maxNumber(list1))

