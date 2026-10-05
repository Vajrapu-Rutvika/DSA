class Solution:
    def findDuplicate(self, nums):
        
        # STEP 1: cycle find
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]              # 1 step
            fast = nums[nums[fast]]        # 2 steps

            if slow == fast:
                break

        # STEP 2: cycle entrance find
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]              # 1 step
            fast = nums[fast]              # 1 step

        return slow