def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    length = len(nums)
    values = [0] * length
    prev1 = 0
    prev2 = 0

    for i in range(length):
        curr = max(nums[i] + prev2, prev1)
        values[i] = curr
        prev2 = prev1
        prev1 = curr

    return max(values)