# stack = []

# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)
# stack.append(5)

# print(stack)

# stack.pop()
# print(stack)



# use the method in for loop stack

stack = []

for i in range(1, 10):
    stack.append(i)
    print(stack)

print("\n")

for i in range(1, 10):
    print(stack.pop())
    print(stack)

