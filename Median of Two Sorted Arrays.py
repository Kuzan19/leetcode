def findMedianSortedArrays(A: list[int], B: list[int]) -> float:
    c = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            c[n] = A[i]
            i += 1
            n += 1
        else:
            c[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        c[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        c[n] = B[k]
        k += 1
        n += 1
    if len(c) % 2 == 0:
        index = (len(c) // 2) - 1
        result = (c[index] + c[index + 1]) / 2.0
        return result
    else:
        index = len(c) // 2
        result = c[index] * 1.0
        return result


if __name__ == "__main__":
    print(findMedianSortedArrays([1, 3], [3, 4]))

