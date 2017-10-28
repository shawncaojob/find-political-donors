#!/usr/bin/python

from heapq import *

class MedianFinder:
  def __init__(self):
    self.small, self.large = [], []
    self.total = 0

  def addNum(self, num):
    heappush(self.large, num)
    heappush(self.small, -heappop(self.large))
    if len(self.large) < len(self.small):
      heappush(self.large, -heappop(self.small))
    self.total += num

  def getMedian(self):
    if not self.large: return 0
    if len(self.large) > len(self.small):
      return self.large[0] 
    else:
      return (self.large[0] - self.small[0]) / 2.0

  def getSize(self):
    return len(self.small) + len(self.large)

  def getTotal(self):
    return self.total
