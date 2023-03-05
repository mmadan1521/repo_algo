
"""
Stack trace for chosen:
                                    ''
   '1'                 '2'                '3'            ...     '6'
'11' '12'...'16'    '21' '22'...'26'   '31' '32'...'36'  ...  '61' '62'...'66'

print_dice_roll_combinations('', 2)
    print_dice_roll_combinations('1', 1)
        print_dice_roll_combinations('11', 0)
        print_dice_roll_combinations('12', 0)
            ...
        print_dice_roll_combinations('16', 0)
    print_dice_roll_combinations('2', 1)
        print_dice_roll_combinations('21', 0)
        print_dice_roll_combinations('22', 0)
            ...
        print_dice_roll_combinations('26', 0)
    ... ... ...
    ... ... ...
    ... ... ...
    print_dice_roll_combinations('6', 1)
        print_dice_roll_combinations('61', 0)
        print_dice_roll_combinations('62', 0)
            ...
        print_dice_roll_combinations('66', 0)
"""
def print_dice_roll_combinations(chosen: str, n: int) -> None:
    """
        - base case
        - choose and explore
        - backtrack (since passing by value, no need to backtrack)
    """
    if (n == 0):
        print(chosen)
    else:
       for i in range(1, 7):
            print_dice_roll_combinations(chosen + str(i), n - 1)

if __name__ == "__main__":
   print_dice_roll_combinations('', 1)
   print_dice_roll_combinations('', 2)
   print_dice_roll_combinations('', 3)
