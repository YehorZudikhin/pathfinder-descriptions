import networkx as nx

def create_graph():
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes
    G.add_node("F4.27",   type="room")
    G.add_node("F4.27_c", type="corridor")
    G.add_node("F4.26",   type="room")
    G.add_node("F4.26_c", type="corridor")
    G.add_node("F4.25",   type="room")
    G.add_node("F4.25_c", type="corridor")
    G.add_node("F4.24",   type="room")
    G.add_node("F4.24_c", type="corridor")
    G.add_node("F4.23",   type="room")
    G.add_node("F4.23_c", type="corridor")
    G.add_node("F4.22",   type="room")
    G.add_node("F4.22_c", type="corridor")
    G.add_node("F4.20",   type="room")
    G.add_node("F4.20_c", type="corridor")
    G.add_node("toilet",  type="wc")
    G.add_node("hall",    type="hall")
    G.add_node("lift",    type="lift")

    # Add directed edges with weights and descriptions between rooms and their respective corridor nodes
    G.add_edge("F4.27", "F4.27_c", weight=1, description="F4.27 to F4.27 corridor")
    G.add_edge("F4.27_c", "F4.27", weight=1, description="F4.27 corridor to F4.27")

    G.add_edge("F4.26", "F4.26_c", weight=1, description="F4.26 to F4.26 corridor")
    G.add_edge("F4.26_c", "F4.26", weight=1, description="F4.26 corridor to F4.26")

    G.add_edge("F4.25", "F4.25_c", weight=1, description="F4.25 to F4.25 corridor")
    G.add_edge("F4.25_c", "F4.25", weight=1, description="F4.25 corridor to F4.25")

    G.add_edge("F4.24", "F4.24_c", weight=1, description="F4.24 to F4.24 corridor")
    G.add_edge("F4.24_c", "F4.24", weight=1, description="F4.24 corridor to F4.24")

    G.add_edge("F4.23", "F4.23_c", weight=1, description="F4.23 to F4.23 corridor")
    G.add_edge("F4.23_c", "F4.23", weight=1, description="F4.23 corridor to F4.23")

    G.add_edge("F4.22", "F4.22_c", weight=1, description="F4.22 to F4.22 corridor")
    G.add_edge("F4.22_c", "F4.22", weight=1, description="F4.22 corridor to F4.22")

    G.add_edge("F4.20", "F4.20_c", weight=1, description="F4.20 to F4.20 corridor")
    G.add_edge("F4.20_c", "F4.20", weight=1, description="F4.20 corridor to F4.20")


    # Add directed edges with weights and descriptions between corridor nodes
    G.add_edge("F4.27_c", "F4.26_c", weight=2, description="F4.27 corridor to F4.26 corridor")
    G.add_edge("F4.26_c", "F4.27_c", weight=2, description="F4.26 corridor to F4.27 corridor")

    G.add_edge("F4.26_c", "F4.25_c", weight=2, description="F4.26 corridor to F4.25 corridor")
    G.add_edge("F4.25_c", "F4.26_c", weight=2, description="F4.25 corridor to F4.26 corridor")

    G.add_edge("F4.25_c", "F4.24_c", weight=2, description="F4.25 corridor to F4.24 corridor")
    G.add_edge("F4.24_c", "F4.25_c", weight=2, description="F4.24 corridor to F4.25 corridor")

    G.add_edge("F4.24_c", "F4.23_c", weight=2, description="F4.24 corridor to F4.23 corridor")
    G.add_edge("F4.23_c", "F4.24_c", weight=2, description="F4.23 corridor to F4.24 corridor")

    G.add_edge("F4.23_c", "F4.22_c", weight=2, description="F4.23 corridor to F4.22 corridor")
    G.add_edge("F4.22_c", "F4.23_c", weight=2, description="F4.22 corridor to F4.23 corridor")

    G.add_edge("F4.22_c", "F4.20_c", weight=2, description="F4.22 corridor to F4.20 corridor")
    G.add_edge("F4.20_c", "F4.22_c", weight=2, description="F4.20 corridor to F4.22 corridor")

    G.add_edge("F4.20_c", "toilet", weight=2, description="F4.20 corridor to toilet")
    G.add_edge("toilet", "F4.20_c", weight=2, description="Toilet to F4.20 corridor")

    G.add_edge("toilet", "hall", weight=2, description="Toilet to hall")
    G.add_edge("hall", "toilet", weight=2, description="Hall to toilet")

    G.add_edge("hall", "lift", weight=2, description="Hall to lift")
    G.add_edge("lift", "hall", weight=2, description="Lift to hall")

    return G

# Extracts the numerical part of a node name, e.g., 'F4.27' -> 27
def extract_room_number(node_name):
    room_number = ''.join(filter(lambda x: x.isdigit() or x == '.', node_name))
    return float(room_number[:4])


# Determines the turn direction based on the room number comparison
def determine_turn_direction(from_node, to_node):
    from_number = extract_room_number(from_node)
    to_number = extract_room_number(to_node)
    if to_number < from_number:
        return 'left'
    elif to_number > from_number:
        return 'right'
    else:
        return 'straight'


def find_shortest_path(graph, start_node, end_node):
    try:
        path = nx.dijkstra_path(graph, start_node, end_node)
        path_edges = [(path[n], path[n + 1]) for n in range(len(path) - 1)]
        descriptions = []
        accumulated_distance = 0
        accumulated_nodes = 0

        for i, edge in enumerate(path_edges):
            current_node, next_node = edge
            edge_data = graph[current_node][next_node]

            if graph.nodes[current_node]['type'] == 'corridor' and graph.nodes[next_node]['type'] == 'corridor':
                # Accumulate distance
                accumulated_distance += edge_data['weight']
                accumulated_nodes += 1

            else:
                # Add accumulated distance to the description
                if accumulated_distance:
                    descriptions.append(f"Go straight for {accumulated_distance} steps, passing {accumulated_nodes} rooms.")
                    accumulated_distance = 0
                    accumulated_nodes = 0

                if graph.nodes[current_node]['type'] == 'room' and graph.nodes[next_node]['type'] == 'corridor':
                    if i < len(path) - 2:  # Ensure there is a node after next_node to compare with
                        next_next_node = path[i + 2]
                        turn_direction = determine_turn_direction(next_node, next_next_node)
                        descriptions.append(f"{edge_data['description']} and turn {turn_direction}")
                        continue

                elif graph.nodes[current_node]['type'] == 'corridor' and graph.nodes[next_node]['type'] == 'room':
                    if i != 0:
                        prev_node = path[i - 1]
                        turn_direction = determine_turn_direction(prev_node, current_node)
                        descriptions.append(f"Turn {turn_direction}, {edge_data['description']}")
                        continue

                # If there is no accumulated distance, add the current edge's description
                descriptions.append(edge_data['description'])
        
        return path, descriptions
    
    except nx.NetworkXNoPath:
        return None, "No path exists between the specified nodes."