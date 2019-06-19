

x = int(input("Please enter a number: "))
if x < 0:
     x = 0
     print('Negative changed to zero')
elif x < 100 and x>50:
    print('50 to 100')
elif x == 1:
    print('One')
else:
    print('More than 100')
