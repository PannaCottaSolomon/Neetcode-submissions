class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if max(temperatures) == min(temperatures):
            return [0] * len(temperatures)
        
        ans = []
        for i, temp in enumerate(temperatures):
            count = i

            while count < len(temperatures) and temperatures[count] <= temp:
                count += 1
            
            if count < len(temperatures):
                ans.append(count - i)
            else:
                ans.append(0)


        return ans