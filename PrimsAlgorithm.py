import heapq

def prims_mst():
    v = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))
    
    adj = {i: [] for i in range(v)}
    print("Enter edges (source destination weight):")
    for _ in range(e):
        u, v_dest, w = map(int, input().split())
        adj[u].append((v_dest, w))
        adj[v_dest].append((u, w))

    # (weight, current_node, parent_node)
    pq = [(0, 0, -1)]
    visited = [False] * v
    mst = []
    total_cost = 0

    while pq and len(mst) < v:
        weight, curr, prev = heapq.heappop(pq)
        
        if visited[curr]:
            continue
            
        visited[curr] = True
        total_cost += weight
        if prev != -1:
            mst.append((prev, curr, weight))
            
        for neighbor, edge_w in adj[curr]:
            if not visited[neighbor]:
                heapq.heappush(pq, (edge_w, neighbor, curr))

    print("\nEdges in MST:", mst)
    print("Total Minimum Cost:", total_cost)

if __name__ == "__main__":
    prims_mst()