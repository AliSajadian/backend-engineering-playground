'''
House robber (dynamic progeamming)
'''

def rob(nums: list[int]) -> int:
    """
    Returns maximum money you can rob without alerting police.
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        current = max(nums[i] + prev2, prev1)
        prev2 = prev1
        prev1 = current

    return prev1


if __name__ == "__main__":
    houses = [1, 2, 4, 3, 1]
    print(rob(houses))

    print("----------------------------------------------------------------")
    houses = [4, 2, 3, 4, 1, 3]
    print(rob(houses))
