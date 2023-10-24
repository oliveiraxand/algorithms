def sortword(word, start=0, end=None):
    if end is None:
        end = len(word)
    if (end - start) > 1:
        mid = (start + end) // 2
        sortword(word, start, end=mid)
        sortword(word, start=mid, end=end)
        merge(word, start, mid, end)
    return word


def merge(word, start, mid, end):
    left = word[start:mid]
    right = word[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            word[general_index] = right[right_index]
            right_index += 1
        elif right_index >= len(right):
            word[general_index] = left[left_index]
            left_index += 1
        elif left[left_index] < right[right_index]:
            word[general_index] = left[left_index]
            left_index += 1
        else:
            word[general_index] = right[right_index]
            right_index += 1


def is_anagram(first_string, second_string):
    # Caso alguma string esteja vazia
    if first_string == '' or second_string == '':
        return ("".join(sortword(list(first_string))),
                "".join(sortword(list(second_string))), False)
    # Pensar em como refatorar esse return depois
    first = sortword(list(first_string.lower()))
    second = sortword(list(second_string.lower()))
    if first == second:
        return ("".join(first), "".join(second), True)

    return ("".join(first), "".join(second), False)
    # raise NotImplementedError


# print(is_anagram('ovo', 'vvoo'))
