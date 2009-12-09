"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""
 
def cycle(n):
  rem = 1 % n
  pattern = [rem,]
  c = 0

  while True:    
    rem = rem * 10 % n
    # this results in a faster lookup than using try...except!
    if rem in pattern:
      return len(pattern[pattern.index(rem):c])      
    else:
      pattern.append(rem)
      c += 1


if __name__ == '__main__':
  tmp_max = 0
  max = 0
  denominator = 1

  for d in range(1,1000):
    tmp_max = cycle(d)
    if max < tmp_max:
      max = tmp_max
      denominator = d
      
      
  print denominator, max