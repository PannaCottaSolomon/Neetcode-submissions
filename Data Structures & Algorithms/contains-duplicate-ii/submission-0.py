class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        i = 0
        j = 1
        window = [nums[i]]
        while j < len(nums):      
            curr = nums[j]      
            if abs(j - i) > k:
                window.remove(nums[i])
                i += 1

            if curr in window:
                return True
            else:
                window.append(curr)
                
            j += 1

        

        return False