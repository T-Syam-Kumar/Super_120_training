class Solution:
    def maxArea(self, height: List[int]) -> int:
        l , r = 0,len(height)-1
        ans = 0
        while l<r:
            h = min(height[l],height[r])
            b = (r-l)
            ans = max(ans,(h*b))
            if height[l]<height[r]:
                l = l + 1
            else:
                r = r - 1
        return ans