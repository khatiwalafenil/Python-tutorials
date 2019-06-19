a = [5, 1, 4, 3]
print (sorted(a))  ## [1, 3, 4, 5]
print (a)  ## [5, 1, 4, 3]

strs = ['aa', 'BB', 'zz', 'CC']
print (sorted(strs))  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print (sorted(strs, reverse=True))   ## ['zz', 'aa', 'CC', 'BB']

strs = ['ccc', 'aaaa', 'd', 'bb']
print (sorted(strs, key=len))  ## ['d', 'bb', 'ccc', 'aaaa']

## "key" argument specifying str.lower function to use for sorting
print (sorted(strs, key=str.lower))  ## ['aa', 'BB', 'CC', 'zz']

