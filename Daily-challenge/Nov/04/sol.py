class Solution:
    def findMinHeightTrees(self, n, edges):
        neighbors = collections.defaultdict(set)
        for v, w in edges:
            neighbors[v].add(w)
            neighbors[w].add(v)
        def maxpath(v, visited):
            visited.add(v)
            paths = [maxpath(w, visited) for w in neighbors[v] if w not in visited]
            path = max(paths or [[]], key=len)
            path.append(v)
            return path
        path = maxpath(0, set())
        path = maxpath(path[0], set())
        m = len(path)
        return path[(m-1)//2:m//2+1]