# coding=utf-8

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, cnt = 0, 1

        for i in xrange(1, len(nums)):
            if nums[idx] == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    idx = i
                    cnt = 1

        return nums[idx]

if __name__ == '__main__':
    print(Solution().majorityElement([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6]))