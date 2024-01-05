def is_palindrome_iterative(word):
    drow = ''
    index = len(word)-1
    if word == '' or not word:
        return False
    while index >= 0:
        drow = drow + word[index]
        index = index - 1
    return drow == word
