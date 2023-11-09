class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      # Using the sorted function built  into python
        return sorted(s) == sorted(t)
