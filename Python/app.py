def stringChallenge(sen, t):
    d = dict()
    for w in sen:
        if w not in d and w.isphanum():
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

s="fun&!! time"
t="t8h7904wc3"
string = stringChallenge(s, t)
print(string)
