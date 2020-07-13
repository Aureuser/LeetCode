import collections, heapq
class Solution:
    def maxProbability(self, n: int, edges: list, succProb: list, start: int, end: int):
        mem = collections.defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            mem[u].append((v, p))
            mem[v].append((u, p))
        # print(mem)
        dist = [0 for _ in range(n)]
        visitd = [False for _ in range(n)]
        queue = []
        heapq.heappush(queue, (-1, start))
        dist[start] = 1

        while queue:
            maxprob, u = heapq.heappop(queue)
            # print(maxprob, u)
            if visitd[u]:
                continue
            visitd[u] = True

            for v, p in mem[u]:
                new_prob = - (p * maxprob)
                if dist[v] < new_prob:
                    dist[v] = new_prob
                    heapq.heappush(queue, (-dist[v], v))

        return dist[end]


if __name__ == '__main__':
    s = Solution()
    score = s.maxProbability(5,
                             [[1, 4], [2, 4], [0, 4], [0, 3], [0, 2], [2, 3]],
                             [0.37, 0.17, 0.93, 0.23, 0.39, 0.04],
                             3,
                             4)

    # 0.21390
    print(score)


