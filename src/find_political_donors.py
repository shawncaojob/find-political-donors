# Main Solution file

# P1 VC(9), * `CMTE_ID`: identifies the flier, which for our purposes is the recipient of this contribution
# P11 VC(9), * `ZIP_CODE`:  zip code of the contributor (we only want the first five digits/characters)
# P14 DATE, * `TRANSACTION_DT`: date of the transaction
# P15 NUM(14,2), * `TRANSACTION_AMT`: amount of the transaction
# P16 VC(9), * `OTHER_ID`: a field that denotes whether contribution came from a person or an entity

from MedianFinder import MedianFinder

if __name__ == "__main__":
  dic, dic2, sortKeys = {}, {}, []
  with open("../input/itcont.txt") as f:
    for line in f:
#      print(line)
      linelist = line.split("|")

      # Ignore lines that not good
      if len(linelist[15].strip()) > 0: continue 

      # Save all vars
      cmte_id = linelist[0]
      zip_code5 = linelist[10] if len(linelist) <= 5 else linelist[10][:5]
      transaction_dt = linelist[13]
      transaction_amt = linelist[14]
      other_id = linelist[15]

      # For Output 2
      key = cmte_id + "_" + transaction_dt
      if key not in dic2:
        sortKeys.append([cmte_id, transaction_dt[4:] + transaction_dt[:4]])
        mh2 = MedianFinder()
      else:
        mh2 = dic2[key]
      dic2[key] = mh2
      mh2.addNum(float(transaction_amt))
      #for k1,v1 in dic2.iteritems():
      #  print(k1, v1.large, v1.small)
      #print("______________")

      # For Output 1
      #print(cmte_id, zip_code5, transaction_dt, transaction_amt, other_id)
      mh = dic.get(zip_code5, MedianFinder())
      dic[zip_code5] = mh
      mh.addNum(float(transaction_amt))
      #print(dic)

      # 1st Output
      print("|".join([cmte_id, zip_code5, str(int(round(mh.getMedian()))), str(mh.getSize()), str(int(round(mh.getTotal())))]))

    print("-------------------")
    # 2nd Output
    #print(sortKeys)
    for row in sorted(sortKeys, key = lambda x: (x[0], x[1])):
      k = row[0] + "_" + row[1][4:] + row[1][:4]
      tmp = [row[0], row[1][4:] + row[1][:4], str(int(round(dic2[k].getMedian()))), str(dic2[k].getSize()), str(int(round(dic2[k].getTotal())))]
      print("|".join(tmp))
