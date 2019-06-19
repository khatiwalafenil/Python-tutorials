# pass by reference, not changing the reference
def reference_test_function (mylist) :
    mylist.append (10)
    print ("List inside the function", mylist)

aList = [1,2,3,4]
reference_test_function(aList)
print ("List outside the function",aList)

# pass by reference and then changing the reference
def reference_change_function (mylist) :
    mylist = [10,20,30]
    print ("List inside the function", mylist)

aList = [1,2,3,4]
reference_change_function(aList)
print ("List outside the function",aList)

