from cgitb import reset
from unittest import result


list1 = [1,2,3,4,5,6,7,8,9]
list2 =[10,20,30,40,50,60]
    
print("List 1 : {}" .format(list1))
print("List 2 : {}" .format(list2))

def list3(list1,list2):
    for i in list2:
        if i%2 == 0:
            list2.remove(i)
    print("Resultant list : {}" .format(list1+list2))

list3(list1,list2)

