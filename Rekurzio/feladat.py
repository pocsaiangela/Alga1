def build_palindrome(chars, left_half, middle_char):
    if not chars:
        return left_half + middle_char + left_half[::-1]
    
    char, count = chars.popitem()
    
    if count % 2 == 1:
        middle_char = char  
        count -= 1
    
    left_half += char * (count // 2)
    
    return build_palindrome(chars, left_half, middle_char)

def create_palindrome_recursive(s):
    char_count = {}
    for char in s:
        char = char.upper()
        if char in char_count.keys():
            char_count[char] += 1
        else:
            char_count[char] = 1

    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    if odd_count > 1:
        return "NO SOLUTION"
    
    return build_palindrome(char_count, "", "")
