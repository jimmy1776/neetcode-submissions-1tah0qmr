class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adjList = {i: [] for i in range(n)}

        visit = set()

        for n1, n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)

        def dfs(i, prev):
            # Base case
            if i in visit:
                return False

            # Recursive case
            visit.add(i)

            for j in adjList[i]:
                if j == prev:
                    continue

                if not dfs(j, i):
                    return False

            return True

        return dfs(0, -1) and n == len(visit)