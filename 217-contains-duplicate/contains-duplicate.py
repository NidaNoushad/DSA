class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prev_map=dict()
        for i,num in enumerate(nums):
            if num in prev_map:
                return True
            else:
                prev_map[num]=i
        return False