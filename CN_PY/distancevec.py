network = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 6, 'C': 3}
}
distance = {}

for node in network:
    distance[node] = {}
    for dest in network:
        if node == dest:
            distance[node][dest] = [0, node]
        elif dest in network[node]:
            distance[node][dest] = [network[node][dest], dest]
        else:
            distance[node][dest] = [float('inf'), None]

def print_table(node):
    print(f"\nRouting Table for Node {node}:")
    print("Destination\tCost\tNext Hop")

    for dest in sorted(distance[node]):
        cost, next_hop = distance[node][dest]
        print(f"{dest}\t\t{cost if cost != float('inf') else '∞'}\t{next_hop}")

updated = True

while updated:
    updated = False

    for node in network:
        for neighbor in network[node]:
            for dest in network:
                new_cost = (
                    network[node][neighbor]
                    + distance[neighbor][dest][0]
                )

                if new_cost < distance[node][dest][0]:
                    distance[node][dest] = [new_cost, neighbor]
                    updated = True
                    
for node in network:
    print_table(node)


#OUTPUT - ALL GIVEN