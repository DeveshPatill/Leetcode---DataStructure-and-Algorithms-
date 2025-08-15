class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):         #length of first forloop startsfrom 0,1,2,3 whichis 2,7,11,15
            for j in range(i+1,len(nums)): #length of second is 1,2,3,4 which is 2,7,11,15
                if nums[i] + nums[j] == target: #check the operation , if true or false
                    return (i,j) 