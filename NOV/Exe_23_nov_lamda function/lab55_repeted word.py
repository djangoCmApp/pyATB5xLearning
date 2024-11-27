# Find first non-repeating char in a string using set
# SWISS --> W is the answer


def first_non_repeat(string):
    for i in string:
        print(string.count(i))
        if string.count(i) == 1:
            return i
    return None

print(first_non_repeat("peppeqqswsqwsxddertr"))