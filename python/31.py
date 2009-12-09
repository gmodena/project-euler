#!/usr/bin/env python

"""
Greedy solution
"""
def ways(change, coins, idx):
  if change == 0:
    return 1
  
  if change < 0 or idx < 0:
    return 0
    
  else:
     return ways(change, coins, idx - 1) + ways(change - coins[idx], coins, idx)
  
  

if __name__ == '__main__':
  coins = [1, 2, 5, 10, 20, 50, 100, 200]
  change = 200
  
  print ways(change, coins, len(coins)-1)