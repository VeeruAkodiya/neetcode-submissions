class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)  # O(n)
        ans = 0

        while numsSet:
            val = next(iter(numsSet))
            numsSet.remove(val)
            count = 1
            right = 1
            left = 1
            while ((val + right) in numsSet):
                numsSet.remove(val+right)
                right += 1
                count += 1
                
            while ((val - left) in numsSet):
                numsSet.remove(val-left)
                left += 1
                count += 1
            ans = max(ans,count)
            
        return ans