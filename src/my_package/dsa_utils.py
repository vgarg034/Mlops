list1 = [1,2,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1,1,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8]


def findLongestDuplicateSequnce(list1):
    counter = 0
    result = []
    foundTheSequence = 'N'
    for i in range(len(list1)-1):

        if list1[i] - list1[i+1] !=0:

            if foundTheSequence == 'Y':
                result.append((list1[i],counter+1))
            counter = 0
            foundTheSequence = 'N'
            continue
        else:
            counter = counter +1
            foundTheSequence = 'Y'
            if i == len(list1)-2:
                result.append((list1[i],counter+1))

    return result 
            

#print(findLongestDuplicateSequnce(list1))
