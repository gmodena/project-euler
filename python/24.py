"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from itertools import permutations

def xcombinations(items=[0,1,2], n=3):
  """
    Compute all possible combinations of items
  """
  if n == 0:
    yield []
    
  else:
    for i in xrange(len(items)):
      for item in xcombinations(items[:i]+items[i+1:], n-1):
        yield [items[i]] + item

def xpermutations(items):
  return xcombinations(items, len(items))


if __name__ == '__main__':
    limit = 999999
    i = 0
    #for l in xpermutations([0,1,2,3,4,5,6,7,8,9]):
    for l in permutations([0,1,2,3,4,5,6,7,8,9], 10):
      if i > limit:
        break
    
      if i == limit:
        print ''.join(map(str,l))

      i += 1
