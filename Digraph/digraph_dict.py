from collections import defaultdict
# implementation of digraph using dict/ adj list
class digraph_dict:

    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V

    def add_edge(self, v, w):
        self.graph[v].append(w)

