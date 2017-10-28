import unittest
from MedianFinder import MedianFinder


class TestSolution(unittest.TestCase):
    def test_0(self):
        nums, target = [1, 2, 3, 4, 5, 6], 3.5
        self.assertEqual(median_finder_factory(nums).getMedian(), target)

    def test_1(self):
        nums, target = [-1, 2, -3, 4, 5, -7, 1], 1
        self.assertEqual(median_finder_factory(nums).getMedian(), target)

    def test_2(self):
        nums, target = [], 0
        self.assertEqual(median_finder_factory(nums).getMedian(), target)


def median_finder_factory(nums):
    mh = MedianFinder()
    for num in nums:
        mh.addNum(num)
    return mh


if __name__ == "__main__":
    unittest.main()
