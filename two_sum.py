class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Time complexity of O(n^2)
        for i in range(len(nums)-1): # Using loop range 0 to length-1
            for j in range(i+1, len(nums)): # Using loop range i+1 to length
                if nums[i] + nums[j] == target: # If i + j = target return 
                    return([i,j])
