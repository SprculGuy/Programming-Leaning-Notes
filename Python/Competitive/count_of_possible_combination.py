# Given the string with A != a
# Need to give O/P in the form od int, that how many combination we can make from user given string

w = input('enter the sting : ')
result = int()

if len(w) >= 1:
    result = 1
else:
    print("Please enter valid string!")

for i in range(1, len(w)+1):
    result = result * i
    
if result > 0:
    print(f'Total number of possible combination we can form are {int(result)}')


