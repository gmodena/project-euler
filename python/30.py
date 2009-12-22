#!/usr/bin/env python

"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""

if __name__ == '__main__':
  
  def max_power(n=1,k=5):
    """
      Return the maximum n digit number m that can be written as a power of 5
    """
    max = 9 ** k
    return n * max
  
  def powers(n="", k=5):
    sum_digits = 0
    for i in n:
      sum_digits += int(i) ** k
      
    return sum_digits
  
  
  sum = 0
  for i in xrange (2, max_power(5,5)):
    if i == powers(str(i)):
      sum += i
      
      
  print "sum: ", sum