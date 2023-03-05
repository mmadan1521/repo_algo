
"""
Stack trace for chosen:
         ''
   '0'         '1'
'00' '01'   '10' '11'


print_binary_combinations('', 2)
    print_binary_combinations('0', 1)
        print_binary_combinations('00', 0)
        print_binary_combinations('01', 0)
    print_binary_combinations('1', 1)
        print_binary_combinations('10', 0)
        print_binary_combinations('11', 0)
"""
def print_binary_combinations(chosen: str, n: int) -> None:
    if (n == 0):
        print(chosen)
    else:
       print_binary_combinations(chosen + '0', n - 1)
       print_binary_combinations(chosen + '1', n - 1)

if __name__ == "__main__":
   print_binary_combinations('', 1)
   print_binary_combinations('', 2)
   print_binary_combinations('', 3)
