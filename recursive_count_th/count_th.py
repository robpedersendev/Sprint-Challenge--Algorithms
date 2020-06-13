'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # if length is less than 2, return 0
    if len(word) < 2:
        return 0
    # if first two letters are th, return 1, continue at index 2
    if word[:2] == 'th':
        return 1 + count_th(word[2:])
    # if first two letters are not th, return 0 and continue at next letter
    else:
        return 0 + count_th(word[1:])


print(count_th('ththth'))
