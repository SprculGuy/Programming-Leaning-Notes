def character_count(s, t):
    d = dict()
    for w in s:
        if w not in d and w.isalpha():
            d[w] = 1
        elif w in d:
            d[w] += 1
        else:
            pass 
        
    s1, string = "",""
    for key, value in d.items():
        s1 += str(value) + key
    if len(s1) == len(t):
        for i,j in zip(s1, t):
            string += i + j

    return string

s="aa3b.bcd@e"
t="fka7529d36"
string = character_count(s, t)
print(string)
