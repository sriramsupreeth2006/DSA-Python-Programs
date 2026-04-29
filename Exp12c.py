# Function to check whether selected vertices form a clique
def is_clique(graph, group):
    for i in range(len(group)):
        for j in range(i + 1, len(group)):
            if group[j] not in graph[group[i]]:
                return False
    return True


# Backtracking to find clique of size k
def find_clique(graph, nodes, k, start, current):
    
    # If k vertices selected
    if len(current) == k:
        if is_clique(graph, current):
            print("Clique found:", current)
            return True
        return False

    for i in range(start, len(nodes)):
        current.append(nodes[i])

        if find_clique(graph, nodes, k, i + 1, current):
            return True

        current.pop()   # Backtrack

    return False


# Driver function
def has_clique(graph, k):
    nodes = list(graph.keys())

    if not find_clique(graph, nodes, k, 0, []):
        print("No clique of size", k, "exists")


# Example graph
graph = {
    1:[2,3,4,5,6],
    2:[1,3,4,5,6],
    3:[1,2,4,5,6],
    4:[1,2,3,5,6],
    5:[1,2,3,4,6],
    6:[1,2,3,4,5]
}

k = 6
has_clique(graph, k)