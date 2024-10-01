import random

def throw (n):
  headcount = 0
  backcount = 0
  for i in range(n):
    if ( random.randint(0,1) == 0):
        headcount += 1
    else:
        backcount += 1
        
  print(f"{headcount/n}")
  print(f"{backcount/n}")

throw(5000)