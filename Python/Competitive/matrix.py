# for 2d matrix
# print the row having max sum

row = int(input('Enter the numer of rows : '))
col = int(input('Enter the numer of columns : '))
matrix = []

for i in range(row):
    a = []
    for j in range(col):
        a.append(int(input(f'Enter the {i}:{j} values for matrix : ')))
    matrix.append(a)

sum = [sum(val) for val in matrix]


print(sum)

    

