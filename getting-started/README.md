## Getting Started

** 1. Python Installation** 
---------------

Install right version of python for your operting system from:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

----
** 2. Checking the python installation **
--------

Once the installtion is done, you should proper installation and version by going in terminal and typing:
```
$ python --version
```

------

**3. using the python shell**
-------

write some inline interpreter code on the python shell. go to your terminal / command prompt and type the following

```
$ python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC
v.1900 64 bit (AMD64)]on win32
Type "help", "copyright", "credits" or "license" for more
information.
>>> print('Hello World');
Hello World
>>> 2 + 2
4
>>> exit()
```

-----


**4. Writing the hello world program:**
----

Lets begin by writing the hello world program:

```
#Just declare the variables on the way
message = "Hello world"
num = 10;

# not the if syntax... there are no brackets
if (num==10) : 
    print message
else:
    print num

```



# The command line arguments

We can get cmd args from the Sys object. We need to import sys for that in the code.
```
import sys
```

once done, we can use `sys.argv` array for the using the arguments

------

** try this code: **

## Getting the arguments in python

```
import sys

print sys.argv

print """Or may be we can go more verbose"""

i = 0;

for arg in sys.argv :
    print i
    print ""+ arg
    i = i+1

print "done"
```
