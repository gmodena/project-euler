#!/usr/bin/env python

if __name__ == '__main__':  
  idx = 1001**2
  sum = 1
  edge = 1000
  angles = 4
  while idx > 1:
    sum += idx
    idx -= edge
    angles -= 1
    
    if angles == 0: # round completed
      edge -= 2 # shirnk the offset
      angles = 4
      

  print sum