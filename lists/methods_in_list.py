list_of_numbers = [10,30,20,50]

## appeding number at the end
print("\n\n Appending the the number at the end")
print("list", list_of_numbers)
list_of_numbers.append (60)
print("list after append", list_of_numbers)


##count number of occurrences
print("\n\n count number of occurrences")
print ("list",list_of_numbers)
print("30 occurs following times in the list:", list_of_numbers.count(30))

## get the index of the element which contains the value
print("\n\n get the index of the element which contains the value")
list_of_numbers.append(20)
print("list", list_of_numbers)
print("First index of element 20 is at : ", list_of_numbers.index(20))

## insert at given index
print("\n\n insert at given index")
print("list", list_of_numbers)
list_of_numbers.insert(3,40)
print("List after inserting 30 at index 3 (fourth position) ", list_of_numbers)

## removing an object from the list
print("\n\n removing an object from the list")
print("list", list_of_numbers)
list_of_numbers.remove(20)
print("list after removing 20: ",list_of_numbers) 
### note what happends to 20

## Reversing the list
print("\n\n Reversing the list") 
print("list: ", list_of_numbers)
list_of_numbers.reverse()
print("reversing the list: ", list_of_numbers)
list_of_numbers.reverse() ## reverting to original


## sorting the list
print("\n\n Sorting the list")
print("list: ", list_of_numbers)
print("sorting the list: ", list_of_numbers.sort())

print ("Sweet!!")



