def stringChallenge(sen):
    largest = ""
    for w in sen.split():   
        if w.isalnum():
            if len(w) > len(largest):
                largest = w
    return largest

s="fun&!! time"
t="t8h7904wc3"
string = stringChallenge(s)
x = 1
for w in string+t:
    if x%3 == 0:
        print("X", end="")
        x += 1
    else:
        print(w, end="")
        x += 1
        