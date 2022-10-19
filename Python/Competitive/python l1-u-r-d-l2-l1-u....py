

n = int(input())
direction = 'r1'
distant = 10
x = 0
y = 0

for i in range(n):
    if direction == 'r1':
        x += distant
        distant += 10
        direction = 'u'
    elif direction == 'u':
        y += distant
        distant += 10
        direction = 'l'
    elif direction == 'l':
        x -= distant
        distant += 10
        direction = 'd'
    elif direction == 'd':
        y -= distant
        distant += 10
        direction = 'r2'
    elif direction == 'r2':
        x += distant
        distant += 10
        direction = 'r1'
    
print(x, end=" ")
print(y)
        
    