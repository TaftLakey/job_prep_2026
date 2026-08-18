def largestInteger(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    subsets = []
    for i in range(0, len(nums) - k+1):
        subsets.append(nums[i:i + k])

    answer = -1

    for i in nums:
        count = 0
        for subset in subsets:
            subset_count = subset.count(i)
            if subset_count != 0:
                count += 1
        if count == 1:
            if i > answer:
                answer = i

    return answer
