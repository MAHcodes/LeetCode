class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums_list = []
        for i in nums:
            if i in nums_list:
                return i
            else:
                nums_list.append(i)