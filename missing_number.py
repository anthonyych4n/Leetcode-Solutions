class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s = set(nums)

        for num in range(len(nums)+1):
            if num not in s:
                return num
                
        # nums = [3,0,1]
        # 0 not in s false, loops into second iteration
        # 1 not in s false, loops into third iteration
        # 2 not in s true, returns num

        # nums = [0,1]
        # 0 not in s false, loops into second iteration
        # 1 not in s false, loops into third iteration
        # 2 not in s true, returns num 