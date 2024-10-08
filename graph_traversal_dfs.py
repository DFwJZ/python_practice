from typing import Dict, List, Set

def has_access(graph: Dict[str, List[str]], user_role: str, target_resource: str) -> bool:
    """
    Perform a depth-first search to determine if a user with a given role
    has access to a specific resource.

    :param graph: A dictionary representing the access control graph
    :param user_role: The starting role of the user
    :param target_resource: The resource we're checking access for
    :return: True if the user has access, False otherwise
    """
    visited: Set[str] = set()

    def dfs(current_role: str) -> bool:
        if current_role == target_resource:
            return True
        
        if current_role in visited:
            return False
        
        visited.add(current_role)

        for neighbor in graph.get(current_role, []):
            if dfs(neighbor):
                return True
        return False
    
    return dfs(user_role)

# Example usage
if __name__ == "__main__":
    # Define the access control graph
    access_graph = {
        "admin": ["read", "write", "delete"],
        "manager": ["read", "write"],
        "user": ["read"],
        "read": ["file1", "file2", "file3"],
        "write": ["file1", "file2"],
        "delete": ["file1"]
    }

    # Test cases
    print(has_access(access_graph, "admin", "file1"))  # Should return True
    print(has_access(access_graph, "user", "file1"))   # Should return True
    print(has_access(access_graph, "user", "file2"))   # Should return True
    print(has_access(access_graph, "user", "delete"))  # Should return False
    print(has_access(access_graph, "manager", "file1"))  # Should return True
    print(has_access(access_graph, "manager", "delete"))  # Should return False