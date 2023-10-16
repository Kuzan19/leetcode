def reverse(x: int) -> int:
    y = str(x)[::-1]
    if str(x)[0] == '-':
        y = int(y[:-1]) * -1
    else:
        y = int(y)
    if y < -2147483647 or y > 2147483647:
        return 0
    return y


if __name__ == "__main__":
    print(reverse(-123))
