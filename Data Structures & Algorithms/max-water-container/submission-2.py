class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0 
        i = 0 
        j = len(heights) - 1
        while i < j:
            # print(i , j)
            smaller = 0 
            if heights[i] > heights[j]:
                smaller = heights[j]
            else:
                smaller = heights[i]

            water  = smaller  * (j - i)
            if water > ans:
                ans = water
            
            if heights[i] > heights[j]:
                j = j - 1
            else:
                i = i + 1
        return ans