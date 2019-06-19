## getting the arguments in python
import sys

print (sys.argv)

print ("""Or may be we can go more verbose""")

i = 0

for arg in sys.argv :
    print (i)
    print (""+ arg)
    i = i+1

print ("done")