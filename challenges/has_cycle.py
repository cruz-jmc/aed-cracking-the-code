def has_cycle(graph: dict[str, list[str]]) -> bool:
    visited = {} # Set to keep track of visited nodes
    recursion_stack = {} # Set to keep track of nodes in the current recursion stack
    def dfs(node: str) -> bool: # Depth-First Search to detect cycles
        if node not in visited:
            visited[node] = True
            recursion_stack[node] = True # base case: if the node is already in the recursion stack, we have a cycle
            for neighbor in graph.get(node, []): # Explore neighbors of the current node
                if neighbor not in visited and dfs(neighbor): # If the neighbor hasn't been visited, recursively visit it
                    return True
                elif recursion_stack.get(neighbor, False): # If the neighbor is in the recursion stack, we have a cycle
                    return True 
        recursion_stack[node] = False
        return False
    for vertex in graph:
        if dfs(vertex):
            return True
    return False