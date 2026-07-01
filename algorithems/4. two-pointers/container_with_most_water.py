'''
Container With Most Water
'''


def maxArea(height: list[int]) -> int:
    '''
    Retrieve max rectangle area obtain by height of 
    2 array element and their indeces distance from each other 
    '''
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water


if __name__ == "__main__":
    numbers_list = [1,8,6,2,5,4,8,3,7]

    print(maxArea(numbers_list))
