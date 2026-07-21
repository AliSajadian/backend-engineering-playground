'''
kth_largest_array_element.py
'''
import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    """
    Returns the kth largest element using a min-heap of size k.
    """
    if not nums:
        return 0

    # Create an empty min-heap
    heap = []

    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif heap[0] < num:
            heapq.heapreplace(heap, num)

    return heap[0]


if __name__ == "__main__":
    numbers_list = [3, 2, 1, 5, 6, 4]
    print(find_kth_largest(numbers_list, 2))

    numbers_list = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    print(find_kth_largest(numbers_list, 4))
