## Solution: Randomized QuickSELECT

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(nums, low, high):
            piv_idx = randint(low, high)
            nums[piv_idx], nums[high] = nums[high], nums[piv_idx]
            piv = nums[high]
            
            i = low - 1
            for j in range(low, high):
                if nums[j] <= piv:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[high], nums[i + 1] = nums[i + 1], nums[high]
            return i + 1
            
        
        def quickselect(nums, k, low, high):
            if low == high:
                return nums[low]
            
            piv_idx = partition(nums, low, high)
            if piv_idx < len(nums) - k:
                return quickselect(nums, k, piv_idx + 1, high)
            elif piv_idx > len(nums) - k:
                return quickselect(nums, k, low, piv_idx - 1)
            else:
                return nums[piv_idx]
        
        return quickselect(nums, k, 0, len(nums) - 1)
