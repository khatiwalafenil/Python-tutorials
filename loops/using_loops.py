## using while loop

c = 0
while (c < 5):
    print (c)
    c = c + 1


## using while loop with else
c = 0
while c < 4:
    print (c)
    c = c + 1
else:
   print ("end value is:", c)
# else is executed with condition becomes false

myString = "Hello World"

for char in myString:
    print (char)

weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

for day in weekdays :
    print (day)

## using else
#Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the list (with for) or 
# when the condition becomes false (with while), but not when the loop is terminated by a break statement.
nums = [1,2,3,4,5]
for n in nums:
    print (n)
else: 
    print (n)


for n in range(5): 
    print (n)

for n in range(2,5):
    print (n)


