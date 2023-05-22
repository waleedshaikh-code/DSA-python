# list in python
# list1 = ['waleed', 'abdullah', 2001, 2023]
# list2 = [1, 2, 3, 4, 5 ]
# list3 = ["a", "b", "c", "d"]

# to print the list value

list1 = ['waleed', 'abdullah', 2001, 2023]
list2 = [1, 2, 3, 4, 5, 6, 7 ]
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5],'\n')

print("to update the list \n")

list = ['waleed', 'abdullah', 2001, 2023]
print ("Value available at index 2 : ")
print (list[2])
list[2] = 2001
print ("New value available at index 2 :  ")
print (list[2],'\n')


print("to delete the value in list \n")

list1 = ['waleed', 'abdullah', 2001, 2023]
print (list1,'\n')
del list1[2]
print ("After deleting value at index 2 : ")
print (list1)