# AND-OR Graph represented as dictionary
graph = {
    "Make Dinner": ("OR", ["Make Pasta", "Make Salad"]),

    "Make Pasta": ("AND", ["Boil Water", "Cook Pasta"]),
    "Make Salad": ("AND", ["Chop Vegetables", "Mix Salad"]),

    # Basic tasks (can succeed/fail)
    "Boil Water": True,
    "Cook Pasta": True,
    "Chop Vegetables": True,
    "Mix Salad": True
}

# Function to solve AND-OR graph
def solve(node):
    
    # If primitive task
    if graph[node] == True:
        print(node, "completed")
        return True

    node_type, children = graph[node]

    # OR Node: choose any one successful path
    if node_type == "OR":
        for child in children:
            print("Trying option:", child)
            if solve(child):
                return True
        return False

    # AND Node: all subtasks must succeed
    elif node_type == "AND":
        for child in children:
            if not solve(child):
                return False
        return True


# Execute plan
if solve("Make Dinner"):
    print("\nValid dinner plan found!")
else:
    print("\nNo valid plan possible.")