
def power(base: int, exp: int) -> int:
    if (exp == 0):
        return 1
    return base * power(base, exp - 1)

if __name__ == "__main__":
    base, exp = 11, 2
    print(f"power({base}^{exp}): {power(base, exp)}")
    base, exp = 11, 3
    print(f"power({base}^{exp}): {power(base, exp)}")
    base, exp = 11, 4
    print(f"power({base}^{exp}): {power(base, exp)}")
