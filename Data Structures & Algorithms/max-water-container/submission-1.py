class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0 
        for i in range(0 , len(heights) - 1):
            for j in range(i + 1, len( heights)):
                # print(i , j)
                smaller = 0 
                if heights[i] > heights[j]:
                    smaller = heights[j]
                else:
                    smaller = heights[i]

                water  = smaller  * (j - i)
                if water > ans:
                    ans = water
        return ans