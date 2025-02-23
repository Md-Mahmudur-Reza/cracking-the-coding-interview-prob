from collections import deque


class Graph:
    def __init__(self):
        self.adjancency_list = {}

    def add(self, src, dst):
        if src not in self.adjancency_list:
            self.adjancency_list[src] = []
        self.adjancency_list[src].append(dst)

    def bfs(self, start, target):
        if start not in self.adjancency_list:
            return False

        queue = deque([start])
        visited = set()

        while queue:
            node = queue.popleft()

            if node == target:
                return True

            if node not in visited:
                visited.add(node)
                queue.extend(self.adjancency_list.get(node, []))

        return False

    def dfs(self, start, target, visited=None):
        if visited is None:
            visited = set()

        if start == target:
            return True

        if start in visited:
            return False

        visited.add(start)

        for neighbor in self.adjancency_list.get(start, []):
            if self.dfs(neighbor, target, visited):
                return True


if __name__ == "__main__":
    graph = Graph()
    graph.add("A", "B")
    graph.add("A", "C")
    graph.add("B", "D")
    graph.add("C", "E")
    graph.add("E", "F")

    print(graph.bfs("A", "F"))
    print(graph.dfs("A", "F"))
