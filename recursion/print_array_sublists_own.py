
"""
Stack trace for 'abc':

print_array_sublists('', 'abc', 0)
    print_array_sublists('a', 'bc', 0)
        print_array_sublists('ab', 'c', 0)
            print_array_sublists('abc', '', 0)
    print_array_sublists('b', 'ac', 1)
        print_array_sublists('bc', 'a', 1)
    print_array_sublists('c', 'ab', 2)
"""
def print_array_sublists(chosen: str, s1: str, j: int) -> None:
    """
        - base case
        - choose and explore
        - backtrack (no need to backtrack as chosen and s1 strings are passed by value in python)
            - otherwise need to remove char at index i from chosen
            - and add char at index i back to s1
            - if we implement this with "list of chars" instead of "string" then backtracking would be neeeded
                - as lists are passed by reference (even in python)
    """
    print(chosen)
    for i in range(j, len(s1)):
        """
            This logic is same as the permutations logic except that don't
            consider the elements before the current chosen elements index.
            i.e. current index is j and don't consider elements before index j
        """
        j = i
        print_array_sublists(chosen + s1[i], s1[:i] + s1[i+1:], j)

if __name__ == "__main__":
    print_array_sublists('', 'a', 0)
    print_array_sublists('', 'ab', 0)
    print_array_sublists('', 'abc', 0)
