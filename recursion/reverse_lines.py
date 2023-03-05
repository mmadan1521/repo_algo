
"""
Open(): Open file and return a corresponding file object.
Since this is a mutable file object, it is passed by reference.

Variables in Python are references to objects.
Most fundamental types in Python are immutable.
    - Numbers, strings, and tuples are the fundamental types that are immutable.
    - whenever int or str variables are modified they point to new memory location.
Mutable objects include:
    - lists, dictionaries and other objects (depending upon their implementation).
"""
def reverse_lines(f) -> None:
       for line in f:
            reverse_lines(f) 
            print(line)

if __name__ == "__main__":
    f = open("file_reverse.txt", "r")
    reverse_lines(f)
    f.close()
