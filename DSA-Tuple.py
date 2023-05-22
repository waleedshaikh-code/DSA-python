# A tuple is a sequence of unchangebale Python objects. 
# Tuples are sequences, just like lists.
# The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.

# tup1 = ('physics', 'chemistry', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5, 6, 7 )
# print ("tup1[0]: ", tup1[0])
# print ("tup2[1:5]: ", tup2[1:5])


# hello = ('waleed', 'shaikh', 2001, 2023)

# print(hello[2])


# tuple2 = (1,2,3,4,5)

# tuple3 = tuple2 + tuple1
# tuple2[2] = 2001            
# # in tuple can't add value like this, this method is only be use in list

# print (tuple2)


# tup = ('waleed', 'abdullah', 2001, 2023)
# print(tup)
# del tup
# print("After deleting tup: ")
# print(tup)                           
# it gives an error buecause after del tup tuple does not exist anymore



countries = ("Spain", "Italy", "Germany", "England", "Turkey")

temp = list(countries)      # convert in list
temp.append("Sweden")       # add item
temp.pop(3)                 # remove item
temp[2] = "Pakistan"        # change item
countries = tuple(temp)     # convert in tuple again
print(countries)

# tuple1 = (0,1,3,2,3,1,3,2,4,5,3)

# res = tuple1.count(3)           # count is use to find the length of given number 
#res = tuple1.index(3)             # it shows the first apperance of the given number
#res = tuple1.index(3, 5, 9)       # it shows the apperance of the given number in the specific positon that we mention (3, 5, 9) here 3 is the num that we find 5 is the startng position and 9 is the ending position like find position num 3 in 4 to 8
# res = len(tuple1)               # len is use to get the length of the tuple


# print('count of 3 in tuple1 is: ', res)

