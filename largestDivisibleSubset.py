def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if (len(nums) <= 1): return nums
        nums = sorted(nums)
        
        res = {}
        
        i = 0
        
        while (i < len(nums)):
            temp = [nums[i]]
            j = i - 1
            while (j >= 0):
                if (nums[i] % nums[j] == 0):
                    if (nums[j] in res):
                        temp = res[nums[j]] + [nums[i]]
                else: temp = [nums[i]]
                j -= 1
                if (nums[i] not in res): res[nums[i]] = temp
                elif (len(temp) > len(res[nums[i]])): res[nums[i]] = temp
                    
            if (nums[i] not in res): res[nums[i]] = temp
                
            i += 1
        return max(res.values(), key=len)

print largestDivisibleSubset([1,2,4,8])