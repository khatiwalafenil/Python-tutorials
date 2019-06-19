# About Lists

Lists are similar to Arrays but can hold any type of consecutive elements in it. Python in excellent in handing operations in list and is one the reason why its is used extensively in data wrangling and analytics

---

# Lets Declare Some Lists

Lets see an example list:

```
# list of strings
list_of_names = ["John","Miller","Tom"]

# list of mulitple types of data
list_of_anything = ["John", 55, "NYC",500.30]

# list of numbers
list_of_numbers = [20,30,10,5,100,70,80]

```
We will be using the above lists for the examples below in python interactive shell. 

---


#List operations

Let's use the lists and see some operations in it.

```
$ python
Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import lists_examples
>>> from lists_examples import list_of_names, list_of_anything, list_of_numbers
```

## Accessing an element in list

User the index number to access the element in the list:

```
>>> print (list_of_names[0])
John
```

## Slicing / Accessing Range of values

We can slice an array from range of indexes. Just mention start index and end index seperated by : inside the square bracket []. The end index is exclusive and will not be included in the slice. For example:

```
>>> print (list_of_numbers[2:3])
[10]
>>> print (list_of_numbers[1:3])
[30, 10]
```

## Delete an Element from the List
Use the del keyword to remove an element from the list and mention the index which needs to be deleted:

```
>>> print (list_of_numbers)
[20, 30, 10, 5, 100, 70, 80]
>>> del list_of_numbers[3]
>>> print (list_of_numbers)
[20, 30, 10, 100, 70, 80]
```

## Get Length of lists
Often in your coding, you will need the length of your list. `len()` function is the rescue for you:

```
>>> len(list_of_numbers)
6
```

## Concate two Lists
Python gives easy `+` operator for concating your lists justs as strings. Lets see it in action:

```
>>> print (list_of_anything + list_of_numbers)
['John', 55, 'NYC', 500.3, 20, 30, 10, 100, 70, 80]
```

## Repetition Operator
You can have your lists repeat its element number of times by using the `*` operator:

```
>>> print (list_of_anything * 2)
['John', 55, 'NYC', 500.3, 'John', 55, 'NYC', 500.3]
```

## The Membership Operator
The `in` keyword is used as the membership operator. It helps you to find whether the element is "in" the list or not:

```
>>> print("is john there in list", 'John' in list_of_anything)
is john there in list True
>>> print("is max there in list", 'Max' in list_of_anything)
is max there in list False
```

