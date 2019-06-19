# lets declare the function with args
def function_with_arguments (arg1, arg2) :
    print (arg1)
    print (arg2)
    return

# call the function with arguments
function_with_arguments ("arg1","arg2")

# What happens if you call without parenthesis ?

function_with_arguments

# lets call function inside print

print (function_with_arguments("1","2"))
## sice function _with_arguments is not returnign anything, it will print none


#lets put function without parenthesis in the print function
print (function_with_arguments)
# it will print the reference of the function. 
# you can say its refering to the reference of the function in the memory
