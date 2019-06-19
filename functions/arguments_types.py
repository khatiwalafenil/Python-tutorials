## required  arguments
def arg_function (arg) :
    a = arg
    return

# below should not work
# arg_function ()

## keyword arguments
def keyword_args (name, age):
    print (name, age)

# this is valid
keyword_args (name="John", age=12)
# and this too in valid
keyword_args (age=12,name="John")


# default arguments
def default_args(name, age=44):
    print (name, age)

default_args ("john") ## its gonna take 44 as default value for age
# or else you can override its value:
default_args("john",55)


# variable length arguments
def var_args (arg1, *varargs):
    print (arg1)
    for arg in varargs:
        print (arg)

var_args (10) # atlease one argument is mandatory

var_args (20,30,40,50)

