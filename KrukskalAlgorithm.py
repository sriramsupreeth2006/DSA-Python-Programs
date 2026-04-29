def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def kruskal_mst():
    v = int(input("Vertices: "))
    e = int(input("Edges: "))
    edges = []
    print("Enter (u v w):")
    for _ in range(e):
        edges.append(list(map(int, input().split())))

    # Sort by weight
    edges.sort(key=lambda x: x[2])
    
    parent = list(range(v))
    mst, min_cost = [], 0

    for u, v_dest, w in edges:
        root_u, root_v = find(parent, u), find(parent, v_dest)
        if root_u != root_v:
            parent[root_u] = root_v
            mst.append((u, v_dest, w))
            min_cost += w

    print("\nMST Edges:", mst)
    print("Total Cost:", min_cost)

if __name__ == "__main__":
    kruskal_mst()