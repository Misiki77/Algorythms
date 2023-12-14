import networkx as nx


class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_vertex(self, vertex):
        self.graph.add_node(vertex)

    def add_edge(self, vertex1, vertex2):
        self.graph.add_edge(vertex1, vertex2)

    def get_neighbors(self, vertex):
        return list(self.graph.successors(vertex))


def topological_sort_dfs(graph):
    visited = set()
    stack = []

    def dfs(vertex):
        if vertex in visited:
            return
        visited.add(vertex)
        for neighbor in graph.get_neighbors(vertex):
            dfs(neighbor)
        stack.append(vertex)

    for vertex in graph.graph.nodes:
        dfs(vertex)

    return stack[::-1]


def main():
    graph = Graph()

    with open("govern.in", "r") as f:
        data = f.readlines()

    for line in data:
        first_word, second_word = line.strip().split()
        graph.add_vertex(first_word)
        graph.add_vertex(second_word)
        graph.add_edge(second_word, first_word)

    print(graph)

    sorted_vertices = topological_sort_dfs(graph)
    sorted_vertices.reverse()

    with open("govern.out", "w") as f:
        for vertex in sorted_vertices:
            f.write(vertex + "\n")


if __name__ == "__main__":
    main()
