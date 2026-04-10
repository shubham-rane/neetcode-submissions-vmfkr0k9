class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = dict()
        # ans = []

        for i in range(0, len(nums)):
            # if nums[i] not in hashmap:
            hashmap[nums[i]] = i
             
                
        
        for i in range(0, len(nums)):
            if target - nums[i] in hashmap:
                j = hashmap[target - nums[i]]
                if i == j:
                    continue
                return [i,j]
        

        