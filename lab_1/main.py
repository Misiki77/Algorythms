def is_subarray(nums1, nums2):
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            i += 1
        j += 1

    return i == len(nums1)


nums1_1 = [1, 2, 3]
nums2_1 = [1, 2, 3, 4]
print(is_subarray(nums1_1, nums2_1))

nums1_2 = [2, 4]
nums2_2 = [1, 2, 3]
print(is_subarray(nums1_2, nums2_2))

nums1_3 = [1, 3, 5]
nums2_3 = [1, 2, 3, 4, 5]
print(is_subarray(nums1_3, nums2_3))