def is_palindrome_recursive(word, low_index, high_index):
    # n = len(word)
    # if n == 1:
    #     return True
    if word == '':
        return False
    if word[low_index] == word[high_index]:
        if high_index <= 1:
            return True
        low = low_index + 1
        high = high_index - 1
        return is_palindrome_recursive(word, low, high)
        # return is_palindrome_recursive(word, low_index=low_index+1,
        # high_index=high_index-1)
    return False
    # if low_index == len(word):
    #     return True
    # is_palindrome_recursive(word, )
    # raise NotImplementedError
# O
# V
# O
