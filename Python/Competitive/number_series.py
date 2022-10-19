# 1,1,2,3,4,9,8,27,...

n = int(input('Enter the number : '))
odd_val, even_val = 0, 0

for i in range(1,n+1):
    if i%2 != 0:
        if i == 1:
            odd_val = 1
        else:
            odd_val = odd_val * 2
    else:
        if i == 2:
            even_val = 1
        else:
            even_val = even_val * 3

if n%2 == 0:
    print(even_val)
else:
    print(odd_val)
