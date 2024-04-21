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

def build_dependencies(data):
    dependencies = {}
    for item in data:
        name = item["name"]
        dep_list = [dep["name"] for dep in item.get("dependent", [])]
        dependencies[name] = dep_list
        for dep in dep_list:
            if dep not in dependencies:
                dependencies[dep] = []  # indicate that this node has no children
    return dependencies

def detect_cycle_in_dependencies(data):
    dependencies = build_dependencies(data)
    visited = {}
    rec_stack = {}
    
    for node in dependencies:
        if not visited.get(node, False):
            if has_cycle(dependencies, node, visited, rec_stack):
                return True
    return False

# example dictionary
data = [{"name":"a", "dependent":[{"name":"b"}, {"name":"c"}]},
        {"name":"c", "dependent":[{"name":"a"}]},
        {"name":"b", "dependent":[]}]

# check for cycles
result = detect_cycle_in_dependencies(data)
print("Cycle detected:", result)

# ************* Module c_3
# results/raw/c_3.py:15:23: W0621: Redefining name 'data' from outer scope (line 38) (redefined-outer-name)
# results/raw/c_3.py:26:33: W0621: Redefining name 'data' from outer scope (line 38) (redefined-outer-name)
# results/raw/c_3.py:43:0: C0103: Constant name "result" doesn't conform to UPPER_CASE naming style (invalid-name)
# -------------------------------------------------------------------
# Your code has been rated at 9.09/10 (previous run: 10.00/10, -0.91)