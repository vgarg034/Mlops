list1 = [2,3,4,1,5,7,5,6,8]
counter = 0
for i in range(len(list1)):
    for j in range(len(list1)):
        counter = counter + 1
print(counter)
counter=0
counteri = 0
for i in range(len(list1)):
    counteri = counteri + 1
    for j in range(i,len(list1)):
        counter = counter + 1
print(counteri)

for i in range(len(list1)):
    for j in range(i):
        print("vineet")
k=3
for i in range(len(list1)-k+1):
    for j in range(i,i+k):
        print("")

for i in range(len(list1)):
    for j in range(i,i+1):
        print()

for i in range(-1,-len(list1)-1,-1):
    print(list1[i])

# condition based movement. for ex - long sequence of duplicate numbers or consecutive numbers sequnce

#list1 = [1,4,3,2,2,2,2,2,2,4,4,2,3,7,7,7,7,7,7,7,7,7,7,7,4,2,1,3]

#print the number having logest duplicate sequence