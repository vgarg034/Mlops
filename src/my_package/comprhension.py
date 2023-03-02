"""
# list comprehension

list1 = [2,3,4,1,5,6,7,8,3,1]

temp_list = [var for var in list1 if var>4]

print(temp_list)



# dictionary comprehension

dic = {'a':1,'b':2,'c':3,'d':'vin'}



dic_test = {k for k in dic.keys()}
print(dic_test)
print(type(dic_test))

dic_test = (k for k in dic.keys())
print(dic_test)
print(type(dic_test))

dic_test = [values for values in dic.values()]
print(dic_test)
print(type(dic_test))
"""


dic = {'a':1,'b':2,'c':3,'d':'vin'}

dic_test = [(k,v) for k,v in dic.items() if k =='d']
print(dic_test)
print(type(dic_test))