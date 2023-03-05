
import sys
import os

# both path and indent are passed by reference
# as str is a immutable datatype
def crawl_dir(path: str, indent: str) -> None:
    # check if path is a directory or file
    if os.path.isfile(path):
        # instead of printing the entire path of the file, just print the filename
        print(f"{indent}{os.path.basename(path)}")
    else:
        print(f"{indent}{path}")
        for file in os.listdir(path):
            # file will only be the file/directory name, so append the path as well
            crawl_dir(os.path.join(path, file), indent + "     ")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("please input a directory path to crawl")
    else:
        ## argv[0] would be program name from "python3 crawl_dir.py <path>"
        path = sys.argv[1]
    
    crawl_dir(path, indent = "")
