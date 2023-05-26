def removeElement(nums, val):
    for num in nums[::-1]:
        if num == val:
            nums.remove(num)

    print(nums)


removeElement(nums=[0, 1, 2, 2, 2, 3, 0, 4, 2], val=2)
