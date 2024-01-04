def is_palindrome_recursive(word, low_index, high_index):
    if not word or word == '':
        return False
    if low_index == high_index or high_index < low_index:
        return True
    elif word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index-1)
    else:
        return False
