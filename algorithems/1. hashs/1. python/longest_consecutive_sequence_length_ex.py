# pylint: disable=broad-except
'''
longest_consecutive_sequence_length.py
Calculating length of longest consecutive seequence
'''
import sys
import re


def get_list_numbers_from_user() -> list[int]:
    '''Read only separated numbers from user'''
    while True:
        try:
            user_input = input("Enter separated interger numbers list: ")

            # Check if any letters exist
            if re.search(r'[a-zA-Z]', user_input):
                print("❌ Letters are not allowed. Please enter numbers only.")
                continue

            numbers = [int(x) for x in re.findall(r'-?\d+', user_input)]

            return numbers, user_input

        except KeyboardInterrupt:
            print("\nProgram exited by user.")
            sys.exit(0)
        except ValueError as e:
            print(f"Invalid input, ${e}")
        except Exception as e:
            print(f"Unexpected error: ${e}")


def get_consecutive_sequences_list(nums: list[int]) -> list[list[int]]:
    '''retrieve list of consecutive sequences'''
    nums_set = set(nums)
    consecutive_sequence_list = []

    while nums_set:
        current_list = []
        n = nums_set.pop()
        current_list.append(n)

        i = n
        while i + 1 in nums_set:
            current_list.append(i + 1)
            nums_set.remove(i + 1)
            i = i + 1

        i = n
        while i - 1 in nums_set:
            current_list.append(i - 1)
            nums_set.remove(i - 1)
            i = i - 1

        consecutive_sequence_list.append(current_list)
    return consecutive_sequence_list


def get_longest_consecutive_sequence_length(nums: list[int]) -> int:
    '''Calculate length of longest consecutive sequence'''
    nums_set = set(nums)
    max_consecutive_sequence_length = 0

    while nums_set:
        current_length = 1
        num = nums_set.pop()

        value = num
        while value + 1 in nums_set:
            nums_set.remove(value + 1)
            current_length += 1
            value += 1

        value = num
        while value - 1 in nums_set:
            nums_set.remove(value - 1)
            current_length += 1
            value -= 1

        max_consecutive_sequence_length = max(max_consecutive_sequence_length, current_length)

    return max_consecutive_sequence_length


if __name__ == "__main__":
    numbers_list, raw_input = get_list_numbers_from_user()
    consecutive_sequesnce_list = get_consecutive_sequences_list(numbers_list)

    print(f"List of cunsecutive sequences in list [{raw_input}] is :{consecutive_sequesnce_list}")

    print(f"Longest cunsecutive sequence length is:\
        {len(max(consecutive_sequesnce_list, key=len)) if consecutive_sequesnce_list else 0}")
