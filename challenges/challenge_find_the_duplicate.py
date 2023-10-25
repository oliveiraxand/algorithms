# def bubble_sort(nums):
#     n = len(nums)

#     for ordered_nums in range(n - 1):
#        for i in range(0, n - 1 - ordered_nums):  # Entender pq assim ele para
#             # no elemento anterior
#             if nums[i] > nums[i + 1]:
#                 nums[i], nums[i + 1] = nums[i + 1], nums[i]
#                 # current = nums[i]
#                 # nums[i] = nums[i + 1]
#                 # nums[i + 1] = current
#     return nums

# def find_duplicate_failed(nums):
#     # orderedNums = nums.sort()
#     ordNums = bubble_sort(nums)
#     n = len(ordNums)
#     counter, numSelected = 0, False
#     for i in range(n - 1):
#         if ordNums[i] == ordNums[i + 1]:
#             if (counter > 0 and numSelected != ordNums[i]) or ordNums[i] < 0:
#                 return False
#             numSelected = ordNums[i]
#             counter += 1
#     return numSelected or False

def check_negative(nums):
    for num in nums:
        if not isinstance(num, int) or num < 0:
            return True
    return False


def find_duplicate(nums):
    """Faça o código aqui."""
    # orderedNums = nums.sort()
    # print(not isinstance(nums, list)) or check_negative(nums))
    if (not isinstance(nums, list)) or check_negative(nums):
        return False
    num_set = set()
    duplicated = False
    for num in nums:
        if num in num_set:
            if duplicated is not False and duplicated != num:
                return False
            duplicated = num
        else:
            num_set.add(num)

    return duplicated
    # raise NotImplementedError


print(find_duplicate(1))
