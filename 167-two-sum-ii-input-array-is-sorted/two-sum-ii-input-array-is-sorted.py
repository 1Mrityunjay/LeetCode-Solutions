class Solution(object):
    def twoSum(self, num, target):
        arr = [(num,i)for i, num in enumerate(num)]
        left = 0
        right = len(arr)-1
        while left<right:
            current_sum = arr[left][0]+arr[right][0]
            if current_sum == target:
                return [arr[left][1]+1, arr[right][1]+1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1 

        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        