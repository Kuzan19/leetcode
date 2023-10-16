def zigzag(s: str, numRows: int):

    if numRows == 1 or numRows >= len(s):
        return s

    rows = [[] for row in range(numRows)]
    index = 0
    step = -1
    for char in s:
        rows[index].append(char)
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step

    for i in range(numRows):
        rows[i] = ''.join(rows[i])
    return ''.join(rows)


if __name__ == "__main__":
    print(zigzag("PAYPALISHIRING", 4))


    # arra = [['P', ' ', ' ', 'I', ' ', ' ', 'N'],
    #         ['A', ' ', 'L', 'S', ' ', 'I', 'G'],
    #         ['Y', 'A', ' ', 'H', 'R', ' ', ' '],
    #         ['P', ' ', ' ', 'I', ' ', ' ', ' '], ]
    # print(arra[0][0], arra[1][0], arra[2][0], arra[3][0],
    #       arra[2][1], arra[1][2],
    #       arra[0][3], arra[1][3], arra[2][3], arra[3][3],
    #       arra[2][4], arra[1][5],
    #       arra[0][6], arra[1][6])