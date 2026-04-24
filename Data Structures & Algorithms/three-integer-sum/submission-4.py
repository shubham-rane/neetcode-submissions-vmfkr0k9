class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        ans = []
        for i in range(0, len(nums) - 2):
            target = 0 - nums[i]
            low = i + 1
            high = len(nums) - 1

            while low < high:
                # print(nums[i], nums[low], nums[high])
                if nums[low] + nums[high] == target:
                    if [nums[i],  nums[low], nums[high]] not in ans:
                        ans.append([nums[i],  nums[low], nums[high]])
                    low = low + 1
                    high = high - 1
                elif nums[low] + nums[high] > target:
                    high = high - 1
                else:
                    low = low + 1

        return ans
        