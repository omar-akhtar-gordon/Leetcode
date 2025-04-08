class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos=0
        nums2 = nums[:]
        for x in range(len(nums)):
            pos=x
            pos=pos+k
            if pos>=len(nums):
                pos=pos%len(nums)
            nums[pos]=nums2[x]