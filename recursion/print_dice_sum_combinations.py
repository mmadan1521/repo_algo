
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
            """
                too small:
                    chosen = [1]
                    current_dice_roll = 1
                    num_of_remaining_dice = 1
                    max_sum = 9
                        Here even we get a 6 on the last dice roll, we can reach max_sum
                        sum_so_far + current_dice_roll + num_of_remaining_dice * 6 >= max_sum):
                             1     +         1         +      1 * 6            = 8      >= 9         
                too big:
                    chosen = [4, 5]
                    current_dice_roll = 3
                    num_of_remaining_dice = 0
                    max_sum = 11
                        Here even we get a 6 on the last dice roll, we can reach max_sum
                        sum_so_far + current_dice_roll + num_of_remaining_dice * 1 <= max_sum):
                             9     +         3         +     0 * 1            = 12     <= 11         
            """
            sum_so_far = sum(chosen)
            num_of_remaining_dice = n - 1
            current_dice_roll = i
            if (sum_so_far + current_dice_roll + num_of_remaining_dice * 1 <= max_sum and
                sum_so_far + current_dice_roll + num_of_remaining_dice * 6 >= max_sum):
                chosen.append(i)
                print_dice_sum_combinations(chosen, n - 1, max_sum)
                chosen.pop(len(chosen) - 1)

if __name__ == "__main__":
   print_dice_sum_combinations(list(), 1, 5)
   print_dice_sum_combinations(list(), 2, 10)
   print_dice_sum_combinations(list(), 3, 12)
