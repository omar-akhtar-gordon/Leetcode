class Solution(object):
    def majorityElement(self, nums):
        count = 0
        major_element = 0
        for i in nums:
            if count == 0:
                major_element = i
            if major_element == i:
                count = count + 1
            else:
                count = count - 1
        return major_element
     