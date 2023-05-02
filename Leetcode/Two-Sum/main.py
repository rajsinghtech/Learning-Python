nums = [2,7,11,15]
target = 9

# Old solution (Brute force)
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return nums[i], nums[j]

# Better solution
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
 

            
first, second = twoSum(nums, target)
print(first, second)
    
