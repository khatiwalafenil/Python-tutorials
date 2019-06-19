# Return some value
def should_return(a, b):
    c = a+b
    return c


print (should_return(1,3))

# Returning nothing 
def no_return(a,b):
    c = a+b

print (no_return(2,2))
## prints None


# lets return but... nothing!
def blank_return (a,b):
    c = a+b
    return c

print (blank_return(2,2))
# once again returns None

# return muliple values
def multi_return (a,b):
    c = a + b
    return a,b,c 

# a shocker for c programmers
print (multi_return(1,3))

print ("done")
