

def function(str, arr):

    for j in range(len(arr)):
        
        if arr[j] in str :
            str = str.replace(arr[j], "")
        
    return str

print(function("Nikita", ['a','i','N','Z']))

