# Stack functionalities

# 1. push - arr.append("item")
# 2. pop - arr.pop()
# 3. top - arr[-1]
# 4. size - len(arr)
# 5. isEmpty - len(arr) < 1

class Stack:
    def __init__(self):
        self.__data = []            # array must be private
    
    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty!!")
            return
        return self.__data.pop()

    def top(self):
        if self.isEmpty():
            print("Stack is Empty!!")
            return
        return self.__data[-1]

    def size(self):
        return len(self.__data)
        
    def isEmpty(self):
        return self.size() == 0

stack = Stack()

print(stack.isEmpty())

stack.push(10)

print(stack.isEmpty())
print(stack.size())
print(stack.top())

stack.pop()

print(stack.isEmpty())