#1. Lets explore variables

#2. Automatic Declaration

slice = 8
type = "Cheese Pizza"
is_available = True

print(slice)
print(type)
print(is_available)

# 3. Redeclaration of Variable


weight = 45.9
print(weight)
# This will print 45.9


weight = "Light"
print(weight)
# This will print Light

# 4. Strongly Typed property
print ("foo" + "bar")

# foobar
print ("foo" + 12)
# TypeError: must be str, not int

print ("foo" + str(12))
# foo12


#5. Global vs Local
weight = "Heavy"
def firstFunction():
    weight = 90
    print(weight)


# This will print 90
firstFunction()

print(weight)
# This will print Heavy


#6. Delete Variable

weight="normal"

del weight


print(weight)
# NameError: name 'weight' is not defined

