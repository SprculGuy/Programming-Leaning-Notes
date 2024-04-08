
a = list(map(int, input().split()))
b = list(map(int, input().split()))

A = list(set(a + b))

B = list(set(a) & set(b))

print(f"[{', '.join(map(str, A))}]")
print(f"[{', '.join(map(str, B))}]")
