import sys


if __name__ == '__main__':
    _, path = sys.argv

    with open(path, 'r', newline=None) as file:
        nums = list(map(int, "".join(file.readlines()).split('\n')))

    nums.sort()

    median = nums[len(nums) // 2]
    result = 0

    for num in nums:
        result += abs(num - median)

    print(result)
