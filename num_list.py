#! python3
## num-list.py || handles number list

import random

class numList:
  def __init__(self, numLen):
    numList = []
    for i in range(numLen):
      numList.append(i+1)
    self.numList = numList
  
  def randomizeNums(self):
    random.shuffle(self.numList)