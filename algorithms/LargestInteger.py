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

def idealLargestInteger(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    length = len(nums)
    freq = [0] * 51

    for i in range(0, length - k + 1):
        subarray = set(nums[i:i + k])
        for num in subarray:
            freq[num] += 1

    ans = -1

    for i in range(50, -1, -1):
        if freq[i] == 1:
            return i