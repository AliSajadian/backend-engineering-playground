'''
longest_substring_without_repeating.py
Retrieve longest unrepeated substring by sliding window
'''
def longest_continuous_uprepwated_substring_length(s: str) -> int:
    '''
    Retrieve longest unrepeated substring length
    '''
    left = 0
    max_len = 0
    last_seen = {}

    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right
        max_len=max(right - left + 1 > max_len)

    return max_len

def longest_continuous_uprepwated_substring(s: str) -> str:
    '''
    Retrieve longest unrepeated substring

    '''
    left = 0
    max_len = 0
    start_idx = 0
    last_seen = {}  # char -> most recent index

    for right, char in enumerate(s):
        # 1️⃣ Check if duplicate exists within current window
        if char in last_seen and last_seen[char] >= left:
            # 2️⃣ Move left pointer just after the duplicate's last position
            left = last_seen[char] + 1

        # 3️⃣ Update the character's latest index
        last_seen[char] = right

        # 4️⃣ Update maximum length and starting index
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start_idx = left

    return s[start_idx:start_idx + max_len]

if __name__ == "__main__":
    SAMPLE_STRING = "abcadeaf"

    print(longest_continuous_uprepwated_substring_length(SAMPLE_STRING))
