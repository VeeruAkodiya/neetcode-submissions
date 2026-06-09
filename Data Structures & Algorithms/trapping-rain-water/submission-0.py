class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        maxl = height[0]
        maxr = height[right]

        while left <= right:
            maxl = max(maxl,height[left])
            maxr = max(maxr,height[right])
            if height[left]<=height[right]:
                ans += 0 if min(maxl,maxr) <= height[left] else min(maxl,maxr) - height[left]
                left += 1
            else:
                ans += 0 if min(maxl,maxr) <= height[right] else min(maxl,maxr) - height[right]
                right -= 1
        return ans