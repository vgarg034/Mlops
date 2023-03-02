list1 = [[1,2,3,4,5,6,7,8,9],[3.4],(4,4),{1:2},0,9.9]

#print(f"type is {type(list1[0])} and value is  {list1[0]}")

#print(f"type is {type(list1[-1])} and value is  {list1[0][1:3]}")

#print(f"type is {type(list1[-1])} and value is  {list1[0][-8:-1]}")

for var in list1:
    #print(type(var))
    #if type(var) == int: 
    #if type(var) == list:
      if type(var) == tuple:
        print(var)

