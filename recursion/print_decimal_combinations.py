
"""
Stack trace for chosen:
                                    ''
   '0'                 '1'                '2'            ...     '9'
'00' '01'...'09'    '10' '11'...'09'   '20' '21'...'29'  ...  '90' '91'...'99'

print_decimal_combinations('', 2)
    print_decimal_combinations('0', 1)
        print_decimal_combinations('00', 0)
        print_decimal_combinations('01', 0)
            ...
        print_decimal_combinations('09', 0)
    print_decimal_combinations('1', 1)
        print_decimal_combinations('10', 0)
        print_decimal_combinations('11', 0)
            ...
        print_decimal_combinations('19', 0)
    ... ... ...
    ... ... ...
    ... ... ...
    print_decimal_combinations('9', 1)
        print_decimal_combinations('90', 0)
        print_decimal_combinations('91', 0)
            ...
        print_decimal_combinations('99', 0)
"""
def print_decimal_combinations(chosen: str, n: int) -> None:
    if (n == 0):
        print(chosen)
    else:
       for i in range(10):
            print_decimal_combinations(chosen + str(i), n - 1)

if __name__ == "__main__":
   print_decimal_combinations('', 1)
   print_decimal_combinations('', 2)
   #print_decimal_combinations('', 3)
