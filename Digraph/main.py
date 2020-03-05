from Digraph.digraph_dict import *
from Digraph.topological_sort import *
from Digraph.dfs import *

gr = digraph_dict(3)
gr.add_edge(0,2)
gr.add_edge(1,0)
gr.add_edge(1,2)
print(gr)
topological_sort(gr)