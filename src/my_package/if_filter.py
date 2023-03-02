# Applicable when list contains numeric data.Airthmetic operatots
# if list1[i] != 0,if list1[i] ==0, if list1[i]>=0, if list1[i]%2==0, if list1[i]//2 ==0 

"""
operaors - > 

logical -> AND , OR , NOT

Membership Operators --> Not in , in 

Arthmetic --> +,-,..

then we have comparispn and assignment operators





"""

"""
list1 = [1,2,6,1,93,3]
print(list1[4]%2)

"""

list1 = ['aeeee','iuabusb','ibgiusg']

if 'a' in list1[0]:
    print("only alphabets")
else:
    print("not alpha")

if 'b' not in list1[0]:
    print("b is not present")

if isinstance(list1[0], int):
    print("data type is string")

if list1[0].startswith('a'):
    print("good")
