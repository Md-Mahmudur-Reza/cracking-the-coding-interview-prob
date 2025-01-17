"""Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?"""


def is_unique(string):
    char_set = []
    char_set = set()
    for char in string:
        if char not in char_set:
            char_set.add(char)
        else:
            return False
    return True
        
if __name__ == "__main__":
    result = is_unique("abc")
    print(result)