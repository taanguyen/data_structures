# uses dfs for graph using linked list implementation
def dfs(v, G, marked, stack):
    neighList = G.adj(v)
    marked[v] = True

    if neighList.head:
        walk = neighList.head
        while walk:
            neigh = walk.value
            if not marked[neigh]:
                marked[neigh] = True
                dfs(neigh, G, marked, stack)
            walk = walk.next
    # push node onto stack, done processing all neighbors
    stack.append(v)