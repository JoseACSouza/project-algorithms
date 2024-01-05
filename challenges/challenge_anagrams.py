def sort_string(s):
    s_list = list(s)
    for i in range(len(s_list)):
        for j in range(i + 1, len(s_list)):
            if s_list[i] > s_list[j]:
                s_list[i], s_list[j] = s_list[j], s_list[i]
    return ''.join(s_list)


def is_anagram(first_string, second_string):

    sorted_first = sort_string(first_string.lower())
    sorted_second = sort_string(second_string.lower())
    if not sorted_first or not sorted_second:
        return (sorted_first, sorted_second, False)
    return (sorted_first, sorted_second, sorted_first == sorted_second)
