
# Space: O(n)
# Time: O(n)

# BFS solution

class Solution:
    def numsSameConsecDiff(self, N, K):

        queue = [i for i in range(10)]

        for i in range(N - 1):
            count = len(queue)
            while count:
                cur_num = queue.pop(0)
                if N > 1 and cur_num == 0:  # handle leading 0 situation
                    count -= 1
                    continue

                tail_number = cur_num % 10
                next_number = {tail_number + K, tail_number - K} # using set to remove duplicate

                for num in next_number:
                    if 0 <= num < 10:
                        queue.append(cur_num * 10 + num)
                count -= 1

        return queue




