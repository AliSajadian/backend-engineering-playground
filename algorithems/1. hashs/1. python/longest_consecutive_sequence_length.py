'''
longest_consecutive_sequence_length_ex.py
Calculating length of longest consecutive seequence
'''
def get_longest_consecutive_sequence_length(nums: list[int]) -> int:
    '''Calculate length of longest consecutive sequence'''
    nums_set = set(nums)
    max_consecutive_sequence_length = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            value = num
            consecutive_sequence_length = 1

            while value + 1 in nums_set:
                value += 1
                consecutive_sequence_length += 1

            if max_consecutive_sequence_length < consecutive_sequence_length:
                max_consecutive_sequence_length = consecutive_sequence_length

    return max_consecutive_sequence_length


if __name__ == "__main__":
    numbers_list = [7, 4, 9, 0, 8, 2, 11, 5, 8, 10]

    print(get_longest_consecutive_sequence_length(numbers_list))
