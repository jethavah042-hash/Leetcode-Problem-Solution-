class Solution(object):
    def nextPermutation(self, nums):
        n = len(nums)

        # STEP 1: find breakpoint
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # STEP 2: swap with next greater element
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # STEP 3: reverse remaining part
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1