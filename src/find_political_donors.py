# Main Solution file

# P1 VC(9), * `CMTE_ID`: identifies the flier, which for our purposes is the recipient of this contribution
# P11 VC(9), * `ZIP_CODE`:  zip code of the contributor (we only want the first five digits/characters)
# P14 DATE, * `TRANSACTION_DT`: date of the transaction
# P15 NUM(14,2), * `TRANSACTION_AMT`: amount of the transaction
# P16 VC(9), * `OTHER_ID`: a field that denotes whether contribution came from a person or an entity

from heapq import *

class MedianHelper:
  def __init__():
    self.small, self.large = [], []
    pass

  def addNum(num):
    heappush(self.large, num)
    heappush(self.small, num)
    pass

  def findMedian():
    return 
      

  

if __name__ == "__main__":
  with open("../input/itcont.txt") as f:
    for line in f:
      print(line)
      linelist = line.split("|")

      # Ignore lines that not good
      if len(linelist[15].strip()) > 0: continue 

      # Save all vars
      cmte_id = linelist[0]
      zip_code5 = linelist[10] if len(linelist) <= 5 else linelist[10][:5]
      transaction_dt = linelist[13]
      transaction_amt = linelist[14]
      other_id = linelist[15]

      print(cmte_id, zip_code5, transaction_dt, transaction_amt, other_id)
      if zip_code5 not in dic:
        dic
      
      
