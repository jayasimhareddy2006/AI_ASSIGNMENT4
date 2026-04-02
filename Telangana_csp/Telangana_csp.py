import networkx as nx
import matplotlib.pyplot as plt

districts = [
"Adilabad","Komaram Bheem","Mancherial","Nirmal","Nizamabad",
"Jagitial","Peddapalli","Karimnagar","Rajanna Sircilla",
"Kamareddy","Medak","Siddipet","Sangareddy","Vikarabad",
"Medchal","Hyderabad","Rangareddy","Mahabubnagar",
"Narayanpet","Wanaparthy","Nagarkurnool","Jogulamba Gadwal",
"Nalgonda","Suryapet","Yadadri","Khammam","Bhadradri",
"Mulugu","Jayashankar","Warangal","Hanamkonda",
"Mahabubabad","Jangaon"
]

neighbors = {

"Adilabad":["Komaram Bheem","Nirmal"],
"Komaram Bheem":["Adilabad","Mancherial"],
"Mancherial":["Komaram Bheem","Jayashankar"],
"Nirmal":["Adilabad","Nizamabad"],

"Nizamabad":["Nirmal","Kamareddy","Jagitial"],
"Jagitial":["Nizamabad","Karimnagar","Peddapalli"],
"Peddapalli":["Jagitial","Karimnagar"],
"Karimnagar":["Jagitial","Peddapalli","Rajanna Sircilla","Siddipet"],
"Rajanna Sircilla":["Karimnagar","Kamareddy","Siddipet"],

"Kamareddy":["Nizamabad","Medak","Rajanna Sircilla","Siddipet"],
"Medak":["Kamareddy","Siddipet","Sangareddy"],
"Siddipet":["Medak","Rajanna Sircilla","Karimnagar","Jangaon","Medchal"],

"Sangareddy":["Medak","Vikarabad","Rangareddy","Medchal"],
"Vikarabad":["Sangareddy","Rangareddy"],

"Rangareddy":["Vikarabad","Medchal","Hyderabad","Mahabubnagar","Nalgonda"],
"Hyderabad":["Rangareddy","Medchal"],
"Medchal":["Hyderabad","Rangareddy","Yadadri","Siddipet","Sangareddy"],

"Yadadri":["Medchal","Nalgonda"],
"Nalgonda":["Yadadri","Suryapet","Nagarkurnool","Rangareddy"],
"Suryapet":["Nalgonda","Khammam"],

"Khammam":["Suryapet","Bhadradri","Mahabubabad","Mulugu"],
"Bhadradri":["Khammam"],

"Mahabubabad":["Khammam","Hanamkonda","Warangal"],
"Hanamkonda":["Mahabubabad","Warangal"],
"Warangal":["Hanamkonda","Mulugu","Jangaon","Mahabubabad"],

"Mulugu":["Warangal","Jayashankar","Khammam"],
"Jayashankar":["Mulugu","Mancherial"],

"Jangaon":["Warangal","Siddipet"],

"Mahabubnagar":["Rangareddy","Narayanpet","Wanaparthy"],
"Narayanpet":["Mahabubnagar"],
"Wanaparthy":["Mahabubnagar","Nagarkurnool","Jogulamba Gadwal"],
"Nagarkurnool":["Wanaparthy","Nalgonda","Jogulamba Gadwal"],
"Jogulamba Gadwal":["Wanaparthy","Nagarkurnool"]

}

colors = ["red","green","blue","yellow"]

def is_valid(node, color, assignment):
    for neighbor in neighbors.get(node, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtracking(assignment):
    if len(assignment) == len(districts):
        return assignment

    node = [d for d in districts if d not in assignment][0]

    for color in colors:
        if is_valid(node, color, assignment):
            assignment[node] = color
            result = backtracking(assignment)
            if result:
                return result
            del assignment[node]

    return None

solution = backtracking({})

print("\nTelangana Map Coloring Solution:\n")
for d in solution:
    print(d, "→", solution[d])

G = nx.Graph()
G.add_nodes_from(districts)

for d in neighbors:
    for n in neighbors[d]:
        G.add_edge(d, n)

node_colors = [solution[node] for node in G.nodes()]

plt.figure(figsize=(14,10))
nx.draw(G,
        with_labels=True,
        node_color=node_colors,
        node_size=1200,
        font_size=8)

plt.savefig("telangana_constraint_graph.png", dpi=300, bbox_inches="tight")
plt.show()
