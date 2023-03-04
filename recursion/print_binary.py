
def print_binary(n: int, binary: []) -> None:
   if (n < 2):
      binary.insert(0, int(n))
      return
   print_binary(n / 2, binary)
   binary.append(0, int(n % 2))

if __name__ == "__main__":
   n, l = 2, []
   print_binary(n, l)
   print(f"binary({n}): {l}")
   n, l = 3, []
   print_binary(n, l)
   print(f"binary({n}): {l}")
   n, l = 4, []
   print_binary(n, l)
   print(f"binary({n}): {l}")
   n, l = 5, []
   print_binary(n, l)
   print(f"binary({n}): {l}")
