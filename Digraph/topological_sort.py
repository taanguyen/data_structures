# implementation of topological sort using dfs
from Digraph.dfs import *
def topo_sort_util(v, G, marked, stack):
    marked[v] = True
    for i in G.graph[v]:
        if not marked[i]:
            topo_sort_util(i, G, marked, stack)
    stack.append(v)

def topological_sort(G):
    marked = [False] * G.V
    stack = []
    for i in range(G.V):
        if not marked[i]:
            topo_sort_util(i, G, marked, stack)
    # return reverse postorder of dfs
    while len(stack):
        print(stack.pop())