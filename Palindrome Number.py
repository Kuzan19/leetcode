def isPalindrome(x: int) -> bool:
    digit = str(x)
    left = 0
    right = -1
    while True:
        if left > len(digit) // 2:
            return True
        if digit[left] != digit[right]:
            return False
        else:
            left += 1
            right -= 1


if __name__ == "__main__":
    print(isPalindrome(1321))
