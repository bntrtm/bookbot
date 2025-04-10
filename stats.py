# returns the number of words in the input string
def count_words(string):
    word_list = string.split()
    return len(word_list)

# returns a dictionary with a key for each character in the input string, paired with its number of appearances.
def count_chars(string):
    chars = {}
    for c in string:
        if c.lower() not in chars:
            chars[c.lower()] = 1
        else:    
            chars[c.lower()] += 1
    return chars

# takes a dictionary of char-int pairs, splits each entry into its own dictionary, and returns a sorted list of them, from greatest-to-lowest int.
def sort_chars(dict):
    dict_list = []
    for c in dict:
        dict_list.append(
            {"character": c, "count": dict[c]}
        )
    return sorted(dict_list, key=lambda x: x["count"], reverse=True)

# PERSONAL NOTE: PYTHON LAMBDAS
# A lambda is an anonymous, one-line function in Python. The general syntax is:
#
# lambda argument: result
#
# So, see the following:
#
# dict_list.sort(key=lambda x: x["count"], reverse=True)
#
# This tells Python:
#
# 1. For each x in the list dict_list, look at the "count" value: x["count"].
# 2. Sort the list based on that "count" value, in descending order (reverse=True).
#
# The lambda x: x["count"] part is what determines how to compare the items—it extracts the "count" value for each dictionary.

