class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        if max(temperatures) == min(temperatures):
            return ans
        
        stack = []
        for i, temp in enumerate(temperatures):
            while len(stack) > 0 and temp > stack[-1][0]:
                stk_temp, stk_i = stack.pop()
                ans[stk_i] = i - stk_i   
                
            temp_info = (temp, i)
            stack.append(temp_info)
            # print(stack)

        return ans