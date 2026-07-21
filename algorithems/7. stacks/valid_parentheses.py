'''
valid_parentheses.py

'''

def valid_parentheses(s: str) -> bool:
    '''
    Check parantheses closed in nested way
    '''
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in pairs.values():
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack

if __name__ == "__main__":
    INSTANSE = "({[]}[])"

    print(valid_parentheses(INSTANSE))
