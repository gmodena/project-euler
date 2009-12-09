"""
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
"""

def load_names(file='data/names.txt'):
  """
    Return a sorted array of names.
  """
  names = []
  fp = open(file, 'r')
  for name in fp.read().split(','):
    name = name.strip('"')
    names.append(name)
  
  return sorted(names)
    
  
def score_names(names):
  """
  Score names according to position.
  """
  i = 1
  scores = 0
  for name in names:
    worth = 0
    for letter in list(name):
      worth += ord(letter) - 64
    
    scores += i * worth
    i += 1
    
  return scores
    
  
  
if __name__ == '__main__':
  print score_names(load_names())