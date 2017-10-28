from random import randint
import datetime
import random


def getYYYY():
  return str(randint(1900, 2017))
def getMM():
  return str(randint(1, 12)).zfill(2)
def getDD():
  return str(randint(1, 31)).zfill(2)
def getYYYYMMDD():
  return "2017" + getMM() + "15"
  #return getYYYY() + getMM() + getDD()

if __name__ == "__main__":
  #A = [["C" + str(randint(10000000, 99999999)), getYYYYMMDD() ]for x in xrange(20)]
  A = [["C12345678", getYYYYMMDD() ]for x in xrange(20)]

  s1 = sorted(A, key = lambda x: (x[0], x[1]))

  for row in s1:
    print(row)

