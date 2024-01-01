class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_amount = 0
        left_pillar = 0
        right_pillar = len(height) - 1
        last_height = 0
        while left_pillar < right_pillar:
            max_amount = max(
                max_amount,
                (right_pillar - left_pillar) * min(height[left_pillar], height[right_pillar]),
            )
            if height[left_pillar] < height[right_pillar]:
                last_height = height[left_pillar]
                left_pillar += 1
                while height[left_pillar] < height[right_pillar] and height[left_pillar] < last_height:
                    left_pillar += 1
            else:
                last_height = height[right_pillar]
                right_pillar -= 1
                while height[right_pillar] < height[left_pillar] and height[right_pillar] < last_height:
                    right_pillar -= 1
        return max_amount