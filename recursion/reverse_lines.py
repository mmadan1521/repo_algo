
def reverse_lines(f) -> None:
       for line in f:
            reverse_lines(f) 
            print(line)

if __name__ == "__main__":
    f = open("file_reverse.txt", "r")
    reverse_lines(f)
    f.close()
