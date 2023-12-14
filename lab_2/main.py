def find_sum(arr, P):
    n = len(arr)

    arr.sort()

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            sum = arr[i] + arr[left] + arr[right]

            if sum == P:
                return True
            elif sum < P:
                left += 1
            else:
                right -= 1

    return False

N = 5
A = [1, 2, 3, 4, 5]
P = 10
result = find_sum(A, P)
print(result)