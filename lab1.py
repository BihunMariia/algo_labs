def isMonotonic(nums):
    increasing = decreasing = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False
        elif nums[i] > nums[i - 1]:
            decreasing = False

    return increasing or decreasing

print(isMonotonic([1, 8, 9, 10, 90, 89.9]))