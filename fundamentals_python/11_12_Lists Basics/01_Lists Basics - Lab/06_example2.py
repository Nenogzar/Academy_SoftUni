################### FROM  zahariev-webbersof ####################
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        middle_index = (left + right) // 2
        middle_element = nums[middle_index]

        if middle_element == target:
            return f'Index - {middle_index}'

        if target > middle_element:
            left = middle_index + 1
        else:
            right = middle_index - 1

    return 'Target is not found!'


nums = [int(x) for x in input().split(', ')]
target = int(input())
print(binary_search(nums, target))