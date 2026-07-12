'''
longest_consecutive_sequence_length_ex.py
Calculating length of longest consecutive seequence
'''
from collections import Counter
import heapq

def top_k_frequent_min_heap(nums: list[int], k: int) -> list[int]:
    '''Retrieve k the most frequent elements of nums'''
    # Step 1: Count frequencies
    num_frequent = Counter(nums)

    # Step 2: Build min-heap of size k
    heap = []
    for num, count in num_frequent.items():
        heapq.heappush(heap, (count, num))
        if len(heap) > k:
            heapq.heappop(heap)

    # Step 3: Extract elements from heap
    return [num for count, num in heap]


def top_k_frequent_bucket_sort(nums: list[int], k: int) -> list[int]:
    '''Retrieve k the most frequent elements of nums'''
    # Step 1: Count frequencies
    freq = Counter(nums)

    # Step 2: Create buckets (index = frequency)
    # Maximum possible frequency is len(nums)
    buckets = [[] for _ in range(len(nums) + 1)]

    # Step 3: Place each number in its frequency bucket
    for num, count in freq.items():
        buckets[count].append(num)

    # Step 4: Collect top k from highest frequency buckets
    result = []
    for i in range(len(buckets)-1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result

    return result


if __name__ == "__main__":
    numbers_list = [4, 4, 4, 4]
    print(top_k_frequent_bucket_sort(numbers_list, 3))
