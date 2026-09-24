class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        start = 0
        longest = 0
        test = 1

        for i in range(len(nums)):
            if i == 0:
                continue
            
            prevNum = nums[i - 1]
            currNum = nums[i]
            # print(prevNum, currNum)
            # print(longest)
            if currNum == prevNum + 1:
                test += 1
            longest = max(longest, test)
                

        return longest