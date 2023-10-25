def is_palindrome_iterative(word):
    """Faça o código aqui."""
    n = len(word)
    count = 0
    if word == '':
        return False
    for i in range(n):
        # print(word)
        # print(word[i], word[n - 1 - i])
        # print(i, n - i - 1, n, count)
        if word[i] == word[n - i - 1]:
            count += 1
            if count == n - 1 or n == 1:
                return True
    return False
    # raise NotImplementedError
