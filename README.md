# To run the code.

```
bash run.sh
```

# Files

find_political_donors.py    Main Program
MedianFinder.py             It is the data structure to store the amount so far and calculate Median effectively. It uses two                             priority queues that one storing the large half and the other one stores the lower half. Median                               can be easily calculated from the top of the priority queues. 
MedianFinderTest.py         Unit tests for MedianFinder class
ValidInput.py               Contain Helper function to validate zip code and date.
ValidInput.py               Unit tests for ValidInput class.

# Basic Ideas

* Loop through the input file line by line

* Use dictionary 1, (zip -> MedianFinder()) to record. Calculate running median and output.

* Use dictionary 2, (cmte_id + date -> MedianFinder()) to record. And use another list (cmid, date) for sorting keys. After all lines have been processed, sort list by cmte_id and date. Then use the sorted cmte_id and date to output the median.
