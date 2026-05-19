class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # 1. Build the adjacency list
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # 2. Track visited nodes
        visited = set()
        components = 0
        
        # 3. Helper function for DFS traversal
        def dfs(node):
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
                    
        # 4. Loop through all nodes to find unvisited components
        for i in range(n):
            if i not in visited:
                components += 1
                visited.add(i)
                dfs(i)
                
        return components