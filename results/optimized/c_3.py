def has_cycle(dependencies, current, visited, rec_stack):
    visited[current] = True
    rec_stack[current] = True

    for neighbor in dependencies[current]:
        if not visited.get(neighbor, False):
            if has_cycle(dependencies, neighbor, visited, rec_stack):
                return True
        elif rec_stack.get(neighbor, False):
            return True
            
    rec_stack[current] = False
    return False

def build_dependencies(project_data):
    dependencies = {}
    for item in project_data:
        name = item["name"]
        dep_list = [dep["name"] for dep in item.get("dependent", [])]
        dependencies[name] = dep_list
        for dep in dep_list:
            if dep not in dependencies:
                dependencies[dep] = []  # indicate that this node has no children
    return dependencies

def detect_cycle_in_dependencies(project_data):
    dependencies = build_dependencies(project_data)
    visited = {}
    rec_stack = {}
    
    for node in dependencies:
        if not visited.get(node, False):
            if has_cycle(dependencies, node, visited, rec_stack):
                return True
    return False

def check_cycles():
    sample_data = [{"name": "a", "dependent": [{"name": "b"}, {"name": "c"}]},
                   {"name": "c", "dependent": [{"name": "a"}]},
                   {"name": "b", "dependent": []}]
    return detect_cycle_in_dependencies(sample_data)

# Running the function and printing the result
if __name__ == "__main__":
    CYCLE_DETECTED = check_cycles()
    print("Cycle detected:", CYCLE_DETECTED)

# -------------------------------------------------------------------
# Your code has been rated at 10.00/10 (previous run: 9.09/10, +0.91)