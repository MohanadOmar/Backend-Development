def twoSum(nums, target):
    for num in enumerate(nums):
        for num2 in enumerate(nums):
            if num[1] + num2[1] == target and num[0] != num2[0]:
                print(num[0], num2[0])


twoSum(nums=[3, 3], target=6)
