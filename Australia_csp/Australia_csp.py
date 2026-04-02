import networkx as nx
import matplotlib.pyplot as plt

states = ["WA", "NT", "QLD", "SA", "NSW", "V", "T"]

neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "QLD"],
    "QLD": ["NT", "SA", "NSW"],
    "SA": ["WA", "NT", "QLD", "NSW", "V"],
    "NSW": ["QLD", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []
}

colors = ["red", "green", "blue"]

def is_valid(state, color, assignment):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtracking(assignment):
    if len(assignment) == len(states):
        return assignment

    unassigned = [s for s in states if s not in assignment][0]

    for color in colors:
        if is_valid(unassigned, color, assignment):
            assignment[unassigned] = color

            result = backtracking(assignment)
            if result:
                return result

            del assignment[unassigned]

    return None

solution = backtracking({})

print("\nAustralia Map Coloring Solution:\n")
for state in solution:
    print(state, "→", solution[state])

G = nx.Graph()

edges = [
    ("WA","NT"),
    ("WA","SA"),
    ("NT","SA"),
    ("NT","QLD"),
    ("SA","QLD"),
    ("SA","NSW"),
    ("SA","V"),
    ("QLD","NSW"),
    ("NSW","V")
]

G.add_nodes_from(states)
G.add_edges_from(edges)

node_colors = [solution[node] for node in G.nodes()]

pos = {
    "WA": (-2,-1),
    "NT": (-1,-1),
    "SA": (-1,0),
    "QLD": (0,-1),
    "NSW": (0,0),
    "V": (0,1),
    "T": (0,2)
}

nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=2000,
    font_size=12,
    font_weight="bold"
)

plt.savefig("australia_constraint_graph.png")
plt.show()
