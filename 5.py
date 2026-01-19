"""5 - Solve a problem using the AO search algorithm on an AND-OR graph and show the solution path."""

graph = {
    'A': [['B', 'C'], ['D']],  # A has two choices: AND(B,C) or OR(D)
    'B': [['E', 'F']],  # B → AND(E,F)
    'C': [],  # terminal
    'D': [],  # terminal
    'E': [],  # terminal
    'F': []  # terminal
}

h = {
    'A': 5,
    'B': 3,
    'C': 2,
    'D': 4,
    'E': 0,
    'F': 0
}  # heuristic


def ao_star(node):
    if not graph[node]:
        return [node]  # terminal node

    min_cost = float('inf')
    best_path = []

    for option in graph[node]:  # each AND-option
        cost = sum(h[n] for n in option)
        if cost < min_cost:
            min_cost = cost
            best_path = option

    solution = [node]
    for n in best_path:
        solution += ao_star(n)

    return solution


path = ao_star('A')
print("AO* solution path:", path)
