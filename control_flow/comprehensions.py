#A list comprehension is a compact way to write an expression that expands to a whole list

nums = [1, 2, 3, 4]
squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]


strs = ['hello', 'and', 'goodbye']
shouting = [ s.upper() + '!!!' for s in strs ]
## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']