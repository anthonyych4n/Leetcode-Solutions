class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Using dictionary to solve with time complexity of O(n)
        saw = {}
        for i, nums in enumerate(nums):
            if target - nums in saw:
                return([saw[target-nums],i])
            elif nums not in saw:
                saw[nums] = i
        
