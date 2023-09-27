nums = [2, 3, 4]
target = 6


def twosum(nums: list[int], target: int) -> str:
    num_dict = {}
    for i, j in enumerate(nums):
        digit = target - j
        if digit in num_dict:
            return [num_dict[digit], i]
        else:
            num_dict[j] = i


def twosum2(nums: list[int], target: int) -> str:
    nums_dict = {}
    for i, j in enumerate(nums):
        digit = target - j
        if digit in nums_dict:
            return [nums_dict[digit], i+1]
        else:
            nums_dict[j] = i + 1


if __name__ == "__main__":
    print(twosum2(nums, target))
