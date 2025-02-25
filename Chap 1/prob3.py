"""URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the utrue"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input:"Mr John Smith   ", 13
Output:Mr%20John%20Smith"""


def urlify(str):
    str_list = list(str.strip())

    for i in range(len(str_list)):
        if str_list[i] == " ":
            str_list[i] = "%20"
    result_str = "".join(str_list)
    print(result_str)


if __name__ == "__main__":
    urlify("  Mr John Smith   ")