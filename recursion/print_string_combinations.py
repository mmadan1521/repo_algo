
"""
Stack trace for chosen for 'abc':
                                    ''
                'a'                                             'b'     'c'
        'aa'                'ab'                ac'
'aaa' 'aab' aac'    'aba' 'abb' 'abc'   'aca', 'acb', 'acc'

print_string_combinations('', 'abc')
    print_string_combinations('a', 'abc')
        print_string_combinations('aa', 'abc')
            print_string_combinations('aaa', 'abc')
            print_string_combinations('aab', 'abc')
            print_string_combinations('aac', 'abc')
        print_string_combinations('ab', 'abc')
            print_string_combinations('aba', 'abc')
            print_string_combinations('abb', 'abc')
            print_string_combinations('abc', 'abc')
        print_string_combinations('ac', 'abc')
            print_string_combinations('aca', 'abc')
            print_string_combinations('acb', 'abc')
            print_string_combinations('acc', 'abc')
    print_string_combinations('b', 'abc')
        print_string_combinations('ba', 'abc')
            print_string_combinations('baa', 'abc')
            print_string_combinations('bab', 'abc')
            print_string_combinations('bac', 'abc')
        print_string_combinations('bb', 'abc')
            print_string_combinations('bba', 'abc')
            print_string_combinations('bbb', 'abc')
            print_string_combinations('bbc', 'abc')
        print_string_combinations('bc', 'abc')
            print_string_combinations('bca', 'abc')
            print_string_combinations('bcb', 'abc')
            print_string_combinations('bcc', 'abc')
    print_string_combinations('c', 'abc')
        print_string_combinations('ca', 'abc')
            print_string_combinations('caa', 'abc')
            print_string_combinations('cab', 'abc')
            print_string_combinations('cac', 'abc')
        print_string_combinations('cb', 'abc')
            print_string_combinations('cba', 'abc')
            print_string_combinations('cbb', 'abc')
            print_string_combinations('cbc', 'abc')
        print_string_combinations('cc', 'abc')
            print_string_combinations('cca', 'abc')
            print_string_combinations('ccb', 'abc')
            print_string_combinations('ccc', 'abc')
"""
def print_string_combinations(chosen: str, s1: str) -> None:
    """
        - base case
        - choose and explore
        - backtrack (no need to backtrack as chosen is passed by value in python)
    """
    if (len(chosen) == len(s1)):
        print(chosen)
    else:
       for char in s1:
            print_string_combinations(chosen + char, s1)

if __name__ == "__main__":
   print_string_combinations('', 'ab')
   print_string_combinations('', 'abc')
