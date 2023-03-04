
def print_stars(n: int) -> None:
   if (n == 0):
      return
   print(f"* ", end='')
   print_stars(n - 1)

if __name__ == "__main__":
   print_stars(10)
   print()
