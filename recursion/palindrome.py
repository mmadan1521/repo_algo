
def palindrome(s1: str) -> bool:
    if len(s1) <= 1:
        return True

    if (s1[0] == s1[-1]):
        return palindrome(s1[1:-1])
    else:
        return False

if __name__ == "__main__":
    s = "aaabbbaaa"
    print(f"palindrome('{s}'): {palindrome(s)}")
    s = "aaaabcaaaa"
    print(f"palindrome('{s}'): {palindrome(s)}")