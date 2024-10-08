from collections import Counter
from typing import List


# Day 1: Implement a simple Caesar cipher
class day1:
    def caesar_cipher(text: str, shift: int) -> str:
        res = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                res += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            elif char.isdigit():
                digit = int(char)
                shifted_digit = (digit + shift) % 10
                res += str(shifted_digit)
            else:
                res += char

        return res
    
    # Day 2: Find the most frequent element in a list
    def most_frequent(arr: List[int]) -> int:
        return Counter(arr).most_common(1)[0][0]

def main():
    practice1 = day1
    string1 = "hello world!1993"
    ciphered_text = practice1.caesar_cipher(string1, 7)
    print(ciphered_text)

if __name__ == '__main__':
    main()