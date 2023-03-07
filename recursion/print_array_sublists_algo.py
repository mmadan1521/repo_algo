
"""
Stack trace for 'abc':

print_array_sublists('', 'abc')
    print_array_sublists('', 'bc') # option-1: ignore the current item
        print_array_sublists('', 'c')
            print_array_sublists('', '')
            print_array_sublists('c', '')
        print_array_sublists('b', 'c')
            print_array_sublists('b', '')
            print_array_sublists('bc', '')
    print_array_sublists('a', 'bc') # option-2: consider the current item
        print_array_sublists('a', 'c')
            print_array_sublists('a', '')
            print_array_sublists('ac', '')
        print_array_sublists('ab', 'c')
            print_array_sublists('ab', '')
            print_array_sublists('abc', '')
"""
def print_array_sublists(chosen: list, l1: list) -> None:
    """
        - base case
        - choose and explore
        - backtrack (no need to backtrack as chosen and l1 strings are passed by value in python)
            - otherwise need to remove char at index i from chosen
            - and add char at index i back to l1
            - if we implement this with "list of chars" instead of "string" then backtracking would be neeeded
                - as lists are passed by reference (even in python)
    """
    if (len(l1) == 0):
        print(chosen)
    else:
        # choose
        item = l1.pop(0)
        # explore
        print_array_sublists(chosen, l1) ## option-1: ignore the current item
        chosen.append(item)
        print_array_sublists(chosen, l1) ## option-2: consider the current item
        # backtrack
        # since lists are passed by reference we need to revert back
        chosen.pop(len(chosen) - 1)
        l1.insert(0, item)

if __name__ == "__main__":
   print_array_sublists([], ['a'])
   print_array_sublists([], ['a', 'b'])
   print_array_sublists([], ['a', 'b', 'c'])
