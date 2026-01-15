def water_jug_dfs(cap1,cap2,target):

    visited = set()
    path =[]

    def dfs(jug1,jug2):

        if (jug1,jug2) in visited:
            return False
        visited.add((jug1,jug2))
        path.append((jug1,jug2))

        if(jug1==target or jug2 == target):
            return True

        if dfs(cap1,jug2):
            return True

        if dfs(jug1,cap2):
            return True

        if dfs(0,jug2):
            return True

        if dfs(jug1,0):
            return True

        pour_amount = min(jug1,cap2-jug2)
        if dfs(jug1 - pour_amount, jug2+pour_amount):
            return True

        pour_amount = min(jug2, cap1 - jug1)
        if dfs(jug1 + pour_amount, jug2 - pour_amount):
            return True

        path.pop()
        return False

    if dfs(0,0):
        return path
    else:
        return None

jug1_capacity = 4
jug2_capacity = 3
target = 2

solution_path = water_jug_dfs(jug1_capacity,jug2_capacity,target)

if solution_path:
    print(f"Solution found for the jugs with capacity {jug1_capacity} and {jug2_capacity}, targeting {target}:")

    for i, (j1,j2) in enumerate(solution_path):
        print(f"Step {i+1}: Jug 1 = {j1}, Jug 2 = {j2}")

else:
    print("No Solution Found")