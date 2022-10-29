class Solution:
    def twoSum(self, nums, target) :
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    pass
                elif target == nums[i] + nums[j]:
                    print(nums[j])
                    return print([i,j])


if __name__ == '__main__':
    main = Solution()
    main.twoSum([3, 2, 4], 6)