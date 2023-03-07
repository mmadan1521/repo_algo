
"""
Stack trace for 'abc':

print_string_anagrams('', 'abc')
    print_string_anagrams('a', 'bc')
        print_string_anagrams('ab', 'c')
            print_string_anagrams('abc', '')
        print_string_anagrams('ac', 'b')
            print_string_anagrams('acb', 'abc')
    print_string_anagrams('b', 'ac')
        print_string_anagrams('ba', 'c')
            print_string_anagrams('bac', 'abc')
        print_string_anagrams('bc', 'a')
            print_string_anagrams('bca', 'abc')
    print_string_anagrams('c', 'ab')
        print_string_anagrams('ca', 'b')
            print_string_anagrams('cab', 'abc')
        print_string_anagrams('cb', 'a')
            print_string_anagrams('cba', 'abc')
"""
def print_string_anagrams(chosen: str, s1: str) -> None:
    """
        - base case
        - choose and explore
        - backtrack (no need to backtrack as chosen and s1 strings are passed by value in python)
            - otherwise need to remove char at index i from chosen
            - and add char at index i back to s1
            - if we implement this with "list of chars" instead of "string" then backtracking would be neeeded
                - as lists are passed by reference (even in python)
    """
    if (len(s1) == 0):
        print(chosen)
    else:
       for i in range(len(s1)):
            print_string_anagrams(chosen + s1[i], s1[:i] + s1[i+1:])

if __name__ == "__main__":
   print_string_anagrams('', 'ab')
   print_string_anagrams('', 'abc')
   print_string_anagrams('', 'madan')
   print_string_anagrams('', 'dhatri')
