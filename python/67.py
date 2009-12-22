#!/usr/bin/env python

"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), 
a 15K text file containing a triangle with one-hundred rows.

NOTE: solves also problem 18.
"""

if __name__ == '__main__':
  fp = open("triangle.txt", 'r')
  
  triangle = []
  for line in fp.readlines():
    row =  map(int, line.strip('\r\n').split(' '))
    triangle.append(row)
    
  fp.close()
  
  for i in xrange(1, len(triangle)):
    last = len(triangle[i])
    
    triangle[i][0] += triangle[i-1][0]
    triangle[i][last-1] += triangle[i-1][last-2]
    
    for j in range(1, last-1):
      triangle[i][j] = max(triangle[i][j] + triangle[i-1][j-1], triangle[i][j] + triangle[i-1][j])
        
  
  print max(triangle[len(triangle)-1])
