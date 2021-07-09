def twoSum(nums, target):
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x != y:
                    if nums[x] + nums[y] == target:
                        return [x, y]

print(twoSum([3, 2, 4], 6))
