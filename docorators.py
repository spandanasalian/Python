def div(a,b):
    if b>a:
        return b/a
    else:
        return a/b
print(div(2,10))


#-----------------------------------------------decorators------------------------------------------------------------------

def check(func):
    def inner(a,b):
        if b>a:
            return b/a
        return func(a,b)
    return inner

@check

def div(a,b):
    return a/b
print(div(20,10))