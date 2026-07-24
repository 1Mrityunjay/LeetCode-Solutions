class Solution(object):
    def twoSum(self, nums, target):
        # 1. Glue each number to its original index: [(number, index)]
        # Example: [2, 7, 11] becomes [(2, 0), (7, 1), (11, 2)]
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        # 2. Sort by the numbers. The original indices stay glued!
        indexed_nums.sort()
        
        left = 0
        right = len(indexed_nums) - 1
        
        while left < right:
            # indexed_nums[left][0] gets the actual number
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            
            if current_sum == target:
                # Target found! Return the original indices from index [1]
                return [indexed_nums[left][1], indexed_nums[right][1]]
                
            elif current_sum < target:
                left += 1
            else:
                right -= 1
