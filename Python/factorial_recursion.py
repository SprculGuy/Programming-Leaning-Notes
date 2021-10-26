
def factorial(n):
    if n == 0:
        return 1
        
    return n * factorial(n-1)
    
print(__name__)                 # Prints out '__main__' as static point of exicution is '__main__' for current module
if __name__ == '__main__':
    n = int(input("Enter the number for calculating Factorial : "))
    print(factorial(n))