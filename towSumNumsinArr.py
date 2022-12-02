class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for fst in range(0, len(nums)):
            for scnd in range(fst+1, len(nums)):
                if nums[scnd] + nums[fst] == target:
                    result.append(fst)
                    result.append(scnd)
                return result
                
nums = [3,3]      
s = Solution()
print(s.twoSum(nums, 6))

            

                    
            