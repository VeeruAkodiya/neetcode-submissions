class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # two iterations one right then left
        size = len(nums)
        ans = [1]*size
        print(ans)
        right = 1
        left = 1
        for i in range(0,size):
            ans[i] = left
            left *= nums[i]
        for j in range(size-1,-1,-1):
            ans[j] = ans[j] * right
            right *= nums[j]
        return ans