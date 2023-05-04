import time


class Solution:
    def naive_approach(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        This will have O(nlogn) time complexity
          1. Sort the array (nlogn)
          2. Get the unique set of the array (n)
          3. Return the third last element of the set
        """
        start_time = time.time()
        nums.sort()
        set_nums = list(set(nums))
        if len(set_nums) < 3:
            exit()
        print("--- %s seconds ---" % (time.time() - start_time))
        return set_nums[-3]

    def better_approach(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        This will have O(n) time complexity
          1. Initiate the variables to store value
          2. Get the unique set of the array (n)
          3. Loop through the set and check if the element is greater than the previous (n)
          4. If it is, then update the variables
          5. Return the third variable
        """
        start_time = time.time()
        first = second = third = float('-inf')
        set_nums = list(set(nums))
        if len(set_nums) < 3:
            exit()
        for num in set_nums:
            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
        print("--- %s seconds ---" % (time.time() - start_time))
        return third
