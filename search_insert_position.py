class Solution:
    def recursive_serach(self, low, high):
        if low<=high:
            mid = low +(high-low)//2
            if self.nums[mid]==self.target:
                return mid
            elif self.nums[mid]<self.target:
                return self.recursive_serach(mid+1, high)
            elif self.nums[mid]>self.target:
                return self.recursive_serach(low, mid-1)
        return low
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        self.nums = nums
        self.target = target 
        
        low, high = 0, len(nums)-1
        if self.target<self.nums[low]:
            return low
        if self.target>self.nums[high]:
            return high+1
        if low<=high:
            return self.recursive_serach(low, high)
            
            
        return low
