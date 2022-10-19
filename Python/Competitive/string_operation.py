str = "HOw are you boy 56"
str = str.lower().split(" ")
string = ""

for word in str:
    for char in word:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            string = string + '%'
        elif char != 'a' or char != 'e' or char != 'i' or char != 'o' or char != 'u':
            string = string + '#'
        else:
            string = string + char
    
for word in string:
    print(word, end='')