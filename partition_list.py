def partition_list(nums, k):
    nums.sort()
    # for i in range(len(nums)):
    #     if nums[i] < k:
    #         continue
    #     elif nums[i] == 3:



arr = [2, 2, 2, 5,2, 2, 2, 2, 5]
k=3


print(partition_list(arr, k))
# [2, 2, 2, 2, 2, 2, 2, 2, 5]
