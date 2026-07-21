'''
Retrieve all subsets of a set
'''
def subsets(nums: list[int]) -> list[list[int]]:
    """
    Returns all possible subsets using backtracking.
    """
    result = []
    current = []

    def backtrack(start: int):
        # Add current subset to result
        result.append(current.copy())  # or current[:]

        # Try adding each remaining element
        for i in range(start, len(nums)):
            # Choose
            current.append(nums[i])

            # Explore
            backtrack(i + 1)

            # Un-choose (backtrack)
            current.pop()

    backtrack(0)
    return result


def subsets_iterative(nums: list[int]) -> list[list[int]]:
    """
    Start with empty set, add each number to all existing subsets.
    """
    result = [[]]
    
    for num in nums:
        # Add num to all existing subsets
        new_subsets = [subset + [num] for subset in result]
        result.extend(new_subsets)
    
    return result


if __name__ == "__main__":
    numbers_list = [3, 2, 1]
    print(subsets(numbers_list))

    print("----------------------------------------------------------------")
    numbers_list = [3, 2, 3, 1]
    print(subsets(numbers_list))
