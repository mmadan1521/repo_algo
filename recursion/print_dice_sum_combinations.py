
"""
Stack trace for chosen:
                                    ''
   '1'                 '2'                '3'            ...     '6'
'11' '12'...'16'    '21' '22'...'26'   '31' '32'...'36'  ...  '61' '62'...'66'

print_dice_sum_combinations('', 2)
    print_dice_sum_combinations('1', 1)
        print_dice_sum_combinations('11', 0)
        print_dice_sum_combinations('12', 0)
            ...
        print_dice_sum_combinations('16', 0)
    print_dice_sum_combinations('2', 1)
        print_dice_sum_combinations('21', 0)
        print_dice_sum_combinations('22', 0)
            ...
        print_dice_sum_combinations('26', 0)
    ... ... ...
    ... ... ...
    ... ... ...
    print_dice_sum_combinations('6', 1)
        print_dice_sum_combinations('61', 0)
        print_dice_sum_combinations('62', 0)
            ...
        print_dice_sum_combinations('66', 0)
"""
def print_dice_sum_combinations(chosen: list, n: int, max_sum: int) -> None:
    """
        - base case
        - choose and explore
        - backtrack
    """
    if (n == 0):
        if sum(chosen) == max_sum:
            print(chosen)
    else:
        for i in range(1, 7):
            if (sum(chosen) <= max_sum - i):
                chosen.append(i)
                print_dice_sum_combinations(chosen, n - 1, max_sum)
                chosen.pop(len(chosen) - 1)

if __name__ == "__main__":
   print_dice_sum_combinations(list(), 1, 5)
   print_dice_sum_combinations(list(), 2, 10)
   print_dice_sum_combinations(list(), 3, 12)
