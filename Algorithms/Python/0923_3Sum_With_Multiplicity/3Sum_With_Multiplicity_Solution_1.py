
# Space: O(n)
# Time: O(n^2)

class Solution:
    def threeSumMulti(self, arr, target):
        arr = sorted(arr)
        visited = set()
        length = len(arr)
        mod = 10 ** 9 + 7
        res = 0
        for i in range(1, length - 1):
            left, right = 0, length - 1

            while left < i < right:
                if arr[left] + arr[i] + arr[right] == target:
                    if (arr[left], arr[i], arr[right]) not in visited:
                        if arr[left] < arr[i] < arr[right]:
                            res += arr.count(arr[left]) * arr.count(arr[i]) * arr.count(arr[right])
                        elif arr[left] == arr[i] < arr[right]:
                            res += arr.count(arr[left]) * (arr.count(arr[i]) - 1) // 2 * arr.count(arr[right])
                        elif arr[left] < arr[i] == arr[right]:
                            res += arr.count(arr[left]) * arr.count(arr[i]) * (arr.count(arr[right]) - 1) // 2
                        elif arr[left] == arr[i] == arr[right]:
                            res += arr.count(arr[left]) * (arr.count(arr[i]) - 1) * (arr.count(arr[right]) - 2) // 6
                        visited.add((arr[left], arr[i], arr[right]))
                    right -= 1
                    left += 1
                elif arr[left] + arr[i] + arr[right] < target:
                    left += 1
                elif arr[left] + arr[i] + arr[right] > target:
                    right -= 1

        return res % mod




