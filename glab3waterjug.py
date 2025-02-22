def Goal(state, target):
    return target in state
def successors(state, cap):
    succ = []
    jug1, jug2 = state
    jug1_cap, jug2_cap = cap
    succ.append((jug1_cap, jug2))
    succ.append((jug1, jug2_cap))
    succ.append((0, jug2))
    succ.append((jug1, 0))
    transfer = min(jug1, jug2_cap - jug2)
    succ.append((jug1 - transfer, jug2 + transfer))
    transfer = min(jug2, jug1_cap - jug1)
    succ.append((jug1 + transfer, jug2 - transfer))
    return succ
def dfs(capacities,target):
    stack=[(0,0)]
    visited=set()
    parent={}
    while stack:
        state=stack.pop()
        if state in visited:
            continue
        visited.add(state)
        if Goal(state,target):
            path=[]
            while state:
                path.append(state)
                state=parent.get(state)
            return path[::-1]
        for successor in successors(state,capacities):
            if successor not in visited:
                stack.append(successor)
                parent[successor]=state
    return None
jug1_cap = 4
jug2_cap = 3
target = 2
solution = dfs((jug1_cap, jug2_cap), target)
if solution:
    print("Solution found:")
    for step in solution:
        print(step)
else:
    print("No solution found.")

           

