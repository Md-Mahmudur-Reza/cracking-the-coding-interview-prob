"""Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin-drome. 
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input:Tact Coa
Output:True (permutations: "taco cat", "atco cta", etc.)"""


def palindrome(str):
    temp_set=set()
    str = str.replace(" ","").lower()
    print(str)

    str_list = list(str)
    for i in str_list:
        if i in temp_set:
            temp_set.remove(i)
        else:
            temp_set.add(i)
    
    if len(temp_set) <2:
        return "True"
    else:
        return "False"


if __name__ == "__main__":
    str = "Tact Coe"
    result = palindrome(str)
    print(result)