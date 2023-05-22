dict = {'name':'Waleed', 'age':22, 'eligible':True}

print(dict)
print(dict.keys())      # .keys() only print the key value like name, age ect. 
print(dict.values())      # .values() print the values which defind in the key like Abdullah, 25 ect.

for key in dict.keys():     # we use this method when we itrate the values
    print(f"The value corresponding to the key {key} is {dict[key]}")






# .update() is use to update the list.

# employes1 = {122: 45, 123: 89, 567: 69, 670: 69}
# employes2 = {222: 88, 566: 90}

# employes1.update(employes2)  # .update() is use to update the list like the items of employes2 is added in employes1

# # employes1.clear()       # .clear() is remove all the items in the list and the list become an empty
# employes1.pop(122)     # .pop() is use to remove the item that we menton
# employes1.popitem()     # .popitem() is use to remove the last item
# del employes1[123]        # del is use to delete the item that we mention

# print(employes1)
