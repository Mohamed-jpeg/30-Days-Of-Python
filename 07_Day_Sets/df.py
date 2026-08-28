# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1)) # set() : st2 - st1
print(st1.difference(st2))# {'item1', 'item4'} => st1\st2  : st2 - st1