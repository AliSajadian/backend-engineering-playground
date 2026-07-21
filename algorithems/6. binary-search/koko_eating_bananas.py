'''
Koko eating banana
'''
import math
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    '''
    Finding minimum eating spead for eating all piles in h hours
    '''
    def hours_needed(speed: int) -> int:
        return sum(math.ceil(pile / speed) for pile in piles)

    low = 1
    high = max(piles)

    if len(piles) > h:
        print("It's impossible")
        return -1

    while low < high:
        mid = (low + high) // 2
        if hours_needed(mid) <= h:
            high = mid
        else:
            low = mid + 1

    return low


if __name__ == "__main__":
    numbers_list = [8,6,2,5,4,8,3,7]

    print(minEatingSpeed(numbers_list, 6))
