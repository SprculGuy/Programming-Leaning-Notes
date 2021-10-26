
def div(a, b):
    return a/b

print(div(2,4))

#To edit/update the dev function using function decorator
def smart_div(func):                   
    def div_update(a, b):
        if a<b:
            a,b = b,a
        return func(a, b)
    return div_update

div_decor = smart_div(div)          #Linking decorator and default function. 
                                    #Calling 'smart_div' with passing 'div' function and storing return value on 'div_decor' variable
print(div_decor(2,4))