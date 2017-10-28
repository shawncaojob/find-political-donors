# Main Solution file

# P1 VC(9), * `CMTE_ID`: identifies the flier, which for our purposes is the recipient of this contribution
# P11 VC(9), * `ZIP_CODE`:  zip code of the contributor (we only want the first five digits/characters)
# P14 DATE, * `TRANSACTION_DT`: date of the transaction
# P15 NUM(14,2), * `TRANSACTION_AMT`: amount of the transaction
# P16 VC(9), * `OTHER_ID`: a field that denotes whether contribution came from a person or an entity

from MedianFinder import MedianFinder
from ValidInput import is_valid_date, is_valid_zip
import sys


def parse_line(L):
    """
    :param L: []
    :return: Tuple
    """
    return L[0], L[10], L[13], L[14], L[15]


def gen_out1_line(dicZipToMh, zip5, transaction_amt):
    """
    :param dicZipToMh: MedianFinder
    :param zip5: String
    :param transaction_amt: String
    :return: []
    """
    mf = dicZipToMh.get(zip5, MedianFinder())
    dicZipToMh[zip5] = mf
    mf.addNum(float(transaction_amt))
    return [cmte_id, zip5, str(int(round(mf.getMedian()))), str(mf.getSize()), str(int(round(mf.getTotal())))]


def gen_out2_line(dicIdDateToMh, keysToSort, cmte_id, transaction_dt, transaction_amt):
    """
    :param dicIdDateToMh: {}
    :param keysToSort: []
    :param cmte_id: String
    :param transaction_dt: String
    :param transaction_amt: String
    :return: None
    """
    key = cmte_id + "_" + transaction_dt
    if key not in dicIdDateToMh:
        keysToSort.append([cmte_id, transaction_dt[4:] + transaction_dt[:4]])
        mh2 = MedianFinder()
    else:
        mh2 = dicIdDateToMh[key]

    dicIdDateToMh[key] = mh2
    mh2.addNum(float(transaction_amt))


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: ./find_political_donors.py <input> <output1> <output2>.")
        exit(255)

    inputFile = sys.argv[1]
    outFile1 = sys.argv[2]
    outFile2 = sys.argv[3]

    dicZipToMh, dicIdDateToMh, keysToSort = {}, {}, []

    with open(inputFile, 'r') as fin, open(outFile1, 'w') as fout1, open(outFile2, 'w') as fout2:
        for line in fin:
            # Pre-process
            cmte_id, zip_code, transaction_dt, transaction_amt, other_id = parse_line(line.split("|"))

            if len(other_id.strip()) > 0: continue  # Input Consideration 1
            if not cmte_id or not transaction_amt: continue               # Input Consideration 1,5

            # Output 1. Generate line and write to file
            if not is_valid_zip(zip_code): continue # Input Consideration 3, 4
            fout1.write("|".join(gen_out1_line(dicZipToMh, zip_code[:5], transaction_amt)) + "\n")

            # Output 2. Generate line
            if not is_valid_date(transaction_dt): continue  # Input Consideration 2
            gen_out2_line(dicIdDateToMh, keysToSort, cmte_id, transaction_dt, transaction_amt)

        # Output 2. Sort and write to file
        for row in sorted(keysToSort, key = lambda x: (x[0], x[1])):
             k = row[0] + "_" + row[1][4:] + row[1][:4]
             tmp = [row[0], row[1][4:] + row[1][:4], str(int(round(dicIdDateToMh[k].getMedian()))), str(
                 dicIdDateToMh[k].getSize()), str(int(round(dicIdDateToMh[k].getTotal())))]
             fout2.write("|".join(tmp) + "\n")