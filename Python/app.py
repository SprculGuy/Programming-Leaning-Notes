n=int(input("Enter the number of terms:"))

Sum=0
a=1
d=2

for i in range(n):
    Sum = Sum + a / d**2
    a+=1
    d+=1

print("The sum of series is",Sum)

