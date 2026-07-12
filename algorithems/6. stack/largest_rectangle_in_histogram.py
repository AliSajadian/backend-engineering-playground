'''
Largest Rectangle in Histogram
'''


def largest_rectangle_area(heights: list[int]) -> int:
    '''
    Add a sentinel bar of height 0 at the end
    This forces all remaining bars to be popped
    '''
    heights = heights + [0]
    stack: list[int] = []
    max_area = 0

    for i, height in enumerate(heights):
        while stack and height < heights[stack[-1]]:
            top = stack.pop()
            left_boundry = stack[-1] if stack else -1
            width = i - left_boundry - 1
            max_area = max(max_area, width * heights[top])

        stack.append(i)

    return max_area


if __name__ == "__main__":
    _heights = [1, 8, 6, 2, 5, 4,8, 3,7]
    print(largest_rectangle_area(_heights))

    _heights = [2,1,5,6,2,3]
    print(largest_rectangle_area(_heights))

    _heights = [2, 4]
    print(largest_rectangle_area(_heights))

    _heights = [2, 1, 2]
    print(largest_rectangle_area(_heights))
