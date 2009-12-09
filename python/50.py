#!/usr/bin/env python

import math  

def prime(n):
  if n == 2:
    return True
  else:
    for i in xrange(2, int(math.sqrt(n))+1):
      if n % i == 0:
        return False
        
    return True

def sumup(primes, sum):
  length = 1
  primel = 0
  primesum = 0
  
  for p in primes:
      if (sum + p) < 1000000:
        sum += p
        length += 1

        # *way* faster than checking if sum in primes
        if prime(sum):
          primesum = sum
          primel = length
      else:
        break

  if primesum > 0:
    return primesum, primel

  return 0, 0
  
if __name__ == '__main__':
  bound = 4000
  
  sum = 0
  maxsum = 0
  length = 0
  maxlength = 0
  primes = []
  
  
  for p in xrange(2,bound+1):
    if prime(p):
      primes.append(p)

  idx = 1
  for p in primes:
    sum, length = sumup(primes[idx:len(primes)], p)
    if length > maxlength:
      maxlength = length
      maxsum = sum
  
    idx += 1

  print maxsum, maxlength
  