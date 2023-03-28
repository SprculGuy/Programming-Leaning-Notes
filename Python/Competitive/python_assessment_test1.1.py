def valid_str(lst):
    count = 0
    for string in lst:
        s = string.split(" ")
        if len(s) > 1:
            for w in s:
                if w.isalpha():
                    if w==s[-1]:
                        print(s)
                        count += 1
        else:
            if s[0].isalpha():
                print(s)
                count += 1
    return count

lst = ["Hello Good Morning", "hell2434o", "India", "abc.com"]

valid = valid_str(lst)
invalid = len(lst) - valid

print("Count of valid", valid)
print("Count of invalid", invalid)