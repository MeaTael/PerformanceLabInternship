import sys

if __name__ == "__main__":
    n = int(sys.argv[1])
    m = int(sys.argv[2])

    permutationMap = {i + 1: 1 + (i + m - 1) % n for i in range(n)}

    result = list()
    result.append("1")
    curr = permutationMap[1]

    while curr != 1:
        result.append(str(curr))
        curr = permutationMap[curr]

    print("".join(result))
