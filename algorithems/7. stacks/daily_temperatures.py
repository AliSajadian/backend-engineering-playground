'''
daily_temperatures.py
for every day determine after how many days weather would be warmer

'''

def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    Returns an array where answer[i] is the number of days to wait
    for a warmer temperature. If no warmer day exists, answer[i] = 0.
    """
    answer: list[int] = [0] * len(temperatures)
    stack: list[int] = []  # Stores indices of temperatures that haven't found a warmer day

    for i, temp in enumerate(temperatures):
        # While stack is not empty and current temp is warmer than
        # the temp at the index on top of the stack
        while stack and temp > temperatures[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index

        # Push current index onto the stack
        stack.append(i)

    return answer


if __name__ == "__main__":
    temps1 = [73, 74, 75, 71, 69, 72, 76, 73]
    print(daily_temperatures(temps1))  # [1, 1, 4, 2, 1, 1, 0, 0]

    # Example 2
    temps2 = [30, 40, 50, 60]
    print(daily_temperatures(temps2))  # [1, 1, 1, 0]

    # Example 3
    temps3 = [60, 50, 40]
    print(daily_temperatures(temps3))  # [0, 0, 0]
