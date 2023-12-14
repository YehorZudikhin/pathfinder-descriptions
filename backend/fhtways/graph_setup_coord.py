import networkx as nx
import math

def create_graph():
    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes
    G.add_node("door_right", coord=(-8, 0), type="door")
    G.add_node("door_left", coord=(-18, 0), type="door")

    G.add_node("F4.27",                 type="room")
    G.add_node("F4.27_c",               type="corridor")

    G.add_node("F4.26",         type="room")
    G.add_node("F4.26_c",       type="corridor")

    G.add_node("F4.25",         type="room")
    G.add_node("F4.25_c",       type="corridor")

    G.add_node("F4.24",         type="room")
    G.add_node("F4.24_c",       type="corridor")

    G.add_node("F4.23",   coord=(-24, 0),      type="room")
    G.add_node("F4.23_c", coord=(-24, -2), type="corridor")

    G.add_node("F4.22",   coord=(-22, 0),      type="room")
    G.add_node("F4.22_c", coord=(-22, -2), type="corridor")

    G.add_node("F4.20",            type="room")
    G.add_node("F4.20_c",    coord=(-19, 0), type="corridor")
    G.add_node("F4.20_conn", coord=(-19, -2),      type="conn")

    G.add_node("F4.01",         type="room")
    G.add_node("F4.08",         type="room")
    G.add_node("F4.01_F4.08_c", coord=(-6, 0), type="corridor")

    G.add_node("F4.02",         coord=(-4, -2), type="room")
    G.add_node("F4.07",         type="room")
    G.add_node("F4.02_F4.07_c", coord=(-4, 0), type="corridor")

    G.add_node("F4.03",         type="room")
    G.add_node("F4.06",         coord=(-2, 2),  type="room")
    G.add_node("F4.03_F4.06_c", coord=(-2, 0), type="corridor")

    G.add_node("F4.04",         type="room")
    G.add_node("F4.05",         type="room")
    G.add_node("F4.04_F4.05_c", coord=(0, 0), type="corridor")

    G.add_node("toilets",             type="toilet")
    G.add_node("stairs_left",        type="stairs")
    G.add_node("stairs_left_conn",  coord=(2, 0), type="conn")
    G.add_node("stairs_middle",      type="stairs")
    G.add_node("stairs_right",      coord=(2, 6), type="stairs")
    G.add_node("stairs_right_conn", coord=(2, 0), type="conn")
    G.add_node("lift",              coord=(-12, -1), type="lift")

    # Add directed edges with weights and descriptions between rooms and their respective corridor nodes
    G.add_edge("F4.27", "F4.27_c", weight=3, description="Öffnen Sie die Tür, verlassen Sie den Raum F4.27, gehen Sie 3 Schritte geradaus, um den Korridor zu erreichen.")
    G.add_edge("F4.27_c", "F4.27", weight=3, description="gehen Sie 3 Schritte geradeaus, öffnen Sie die Tür, um den Raum F4.27 zu erreichen.")

    G.add_edge("F4.26", "F4.26_c", weight=2, description="Öffnen Sie die Tür, verlassen Sie den Raum F4.26, gehen Sie 2 Schritte geradaus, um den Korridor zu erreichen.")
    G.add_edge("F4.26_c", "F4.26", weight=2, description="gehen Sie 2 Schritte geradeaus, öffnen Sie die Tür, um den Raum F4.26 zu erreichen.")

    G.add_edge("F4.25", "F4.25_c", weight=2, description="Öffnen Sie die Tür, verlassen Sie den Raum F4.25, gehen Sie 2 Schritte geradaus, um den Korridor zu erreichen.")
    G.add_edge("F4.25_c", "F4.25", weight=2, description="gehen Sie 2 Schritte geradeaus, öffnen Sie die Tür, um den Raum F4.25 zu erreichen.")

    G.add_edge("F4.24", "F4.24_c", weight=2, description="Öffnen Sie die Tür, verlassen Sie den Raum F4.24, gehen Sie 2 Schritte geradaus, um den Korridor zu erreichen.")
    G.add_edge("F4.24_c", "F4.24", weight=2, description="gehen Sie 2 Schritte geradeaus, öffnen Sie die Tür, um den Raum F4.24 zu erreichen.")

    G.add_edge("F4.23", "F4.23_c", weight=2, description="Öffnen Sie die Tür, verlassen Sie den Raum F4.23, gehen Sie 2 Schritte geradaus, um den Korridor zu erreichen.")
    G.add_edge("F4.23_c", "F4.23", weight=2, description="gehen Sie 2 Schritte geradeaus, öffnen Sie die Tür, um den Raum F4.23 zu erreichen.")

    G.add_edge("F4.22", "F4.22_c", weight=2, description="Öffnen Sie die Tür, verlassen Sie den Raum F4.22, gehen Sie 2 Schritte geradaus, um den Korridor zu erreichen.")
    G.add_edge("F4.22_c", "F4.22", weight=2, description="gehen Sie 2 Schritte geradeaus, öffnen Sie die Tür, um den Raum F4.22 zu erreichen.")

    G.add_edge("F4.20", "F4.20_c", weight=1, description="Öffnen Sie die Tür, verlassen Sie den Raum F4.20, gehen Sie 2 Schritte geradaus, um den Korridor zu erreichen.")
    G.add_edge("F4.20_c", "F4.20", weight=1, description="gehen Sie 2 Schritte geradeaus, öffnen Sie die Tür, um den Raum F4.21 zu erreichen.")

    G.add_edge("F4.08", "F4.01_F4.08_c", weight=2, description="Öffnen Sie die Tür, verlassen Sie den Raum F4.08, gehen Sie 2 Schritte geradaus, um den Korridor zu erreichen.")
    G.add_edge("F4.01_F4.08_c", "F4.08", weight=2, description="gehen Sie 2 Schritte geradeaus, öffnen Sie die Tür, um den Raum F4.08 zu erreichen.")

    G.add_edge("F4.07", "F4.02_F4.07_c", weight=2, description="Öffnen Sie die Tür, verlassen Sie den Raum F4.07, gehen Sie 2 Schritte geradaus, um den Korridor zu erreichen.")
    G.add_edge("F4.02_F4.07_c", "F4.07", weight=2, description="gehen Sie 2 Schritte geradeaus, öffnen Sie die Tür, um den Raum F4.07 zu erreichen.")

    G.add_edge("F4.06", "F4.03_F4.06_c", weight=2, description="Öffnen Sie die Tür, verlassen Sie den Raum F4.06, gehen Sie 2 Schritte geradaus, um den Korridor zu erreichen.")
    G.add_edge("F4.03_F4.06_c", "F4.06", weight=2, description="gehen Sie 2 Schritte geradeaus, öffnen Sie die Tür, um den Raum F4.06 zu erreichen.")

    G.add_edge("F4.05", "F4.04_F4.05_c", weight=3, description="Öffnen Sie die Tür, verlassen Sie den Raum F4.05, gehen Sie 3 Schritte geradaus, um den Korridor zu erreichen.")
    G.add_edge("F4.04_F4.05_c", "F4.05", weight=3, description="gehen Sie 3 Schritte geradeaus, öffnen Sie die Tür, um den Raum F4.05 zu erreichen.")

    G.add_edge("F4.04", "F4.04_F4.05_c", weight=3, description="Öffnen Sie die Tür, verlassen Sie den Raum F4.04, gehen Sie 3 Schritte geradaus, um den Korridor zu erreichen.")
    G.add_edge("F4.04_F4.05_c", "F4.04", weight=3, description="gehen Sie 3 Schritte geradeaus, öffnen Sie die Tür, um den Raum F4.04 zu erreichen.")

    G.add_edge("F4.03", "F4.03_F4.06_c", weight=2, description="Öffnen Sie die Tür, verlassen Sie den Raum F4.03, gehen Sie 2 Schritte geradaus, um den Korridor zu erreichen.")
    G.add_edge("F4.03_F4.06_c", "F4.03", weight=2, description="gehen Sie 2 Schritte geradeaus, öffnen Sie die Tür, um den Raum F4.03 zu erreichen.")

    G.add_edge("F4.02", "F4.02_F4.07_c", weight=2, description="Öffnen Sie die Tür, verlassen Sie den Raum F4.02, gehen Sie 2 Schritte geradaus, um den Korridor zu erreichen.")
    G.add_edge("F4.02_F4.07_c", "F4.02", weight=2, description="gehen Sie 2 Schritte geradeaus, öffnen Sie die Tür, um den Raum F4.02 zu erreichen.")

    G.add_edge("F4.01", "F4.01_F4.08_c", weight=2, description="Öffnen Sie die Tür, verlassen Sie den Raum F4.01, gehen Sie 2 Schritte geradaus, um den Korridor zu erreichen,.")
    G.add_edge("F4.01_F4.08_c", "F4.01", weight=2, description="gehen Sie 2 Schritte geradeaus, öffnen Sie die Tür, um den Raum F4.01 zu erreichen.")


    # Add directed edges with weights and descriptions between corridor nodes
    G.add_edge("stairs_left_conn", "stairs_left", weight=6, description="Öffnen Sie die Tür und Sie erreichen den Korridor. Biegen Sie dann nach rechts ab und machen Sie 4 Schritte geradeaus. Biegen Sie dann nach links ab und gehen Sie noch 3 Schritte geradeaus weiter.")
    G.add_edge("stairs_left", "stairs_left_conn", weight=6, description="Gehen Sie 3 Schritte geradeaus, biegen Sie dann nach rechts ab und gehen Sie geradeaus weiter bis zum Ende des Ganges. Die Tür, die zu den Treppen führt, liegt dann auf der linken Seite.")

    G.add_edge("stairs_left", "F4.27_c", weight=2, description="Öffnen Sie die Tür und Sie erreichen den Korridor. Biegen Sie dann nach rechts ab und machen Sie 4 Schritte geradeaus. Biegen Sie dann nach links ab und gehen Sie noch 3 Schritte geradeaus weiter.")
    G.add_edge("F4.27_c", "stairs_left", weight=2, description="Gehen Sie 3 Schritte geradeaus, biegen Sie dann nach rechts ab und gehen Sie geradeaus weiter bis zum Ende des Ganges. Die Tür, die zu den Treppen führt, liegt dann auf der linken Seite.")

    G.add_edge("F4.27_c", "F4.26_c", weight=3, description="Gehen Sie 2 Schritte geradeaus im Korridor.")
    G.add_edge("F4.26_c", "F4.27_c", weight=3, description="Gehen Sie 2 Schritte geradeaus im Korridor.")

    G.add_edge("F4.26_c", "F4.25_c", weight=3, description="Gehen Sie 2 Schritte geradeaus im Korridor.")
    G.add_edge("F4.25_c", "F4.26_c", weight=3, description="Gehen Sie 2 Schritte geradeaus im Korridor.")

    G.add_edge("F4.25_c", "F4.24_c", weight=3, description="Gehen Sie 2 Schritte geradeaus im Korridor.")
    G.add_edge("F4.24_c", "F4.25_c", weight=3, description="Gehen Sie 2 Schritte geradeaus im Korridor.")

    G.add_edge("F4.24_c", "F4.23_c", weight=3, description="Gehen Sie 2 Schritte geradeaus im Korridor.")
    G.add_edge("F4.23_c", "F4.24_c", weight=3, description="Gehen Sie 2 Schritte geradeaus im Korridor.")

    G.add_edge("F4.23_c", "F4.22_c", weight=3, description="Gehen Sie 2 Schritte geradeaus im Korridor.")
    G.add_edge("F4.22_c", "F4.23_c", weight=3, description="Gehen Sie 2 Schritte geradeaus im Korridor.")

    G.add_edge("F4.22_c", "F4.20_conn", weight=3, description="Gehen Sie 2 Schritte geradeaus im Korridor, biegen Sie dann links ab, gehen Sie weitere 2 Schritte und biegen Sie rechts ab.")
    G.add_edge("F4.20_conn", "F4.22_c", weight=3, description="F4.20_conn to F4.22_c.")

    G.add_edge("F4.20_conn", "F4.20_c", weight=3, description="Gehen Sie 2 Schritte geradeaus im Korridor, biegen Sie dann links ab, gehen Sie weitere 2 Schritte und biegen Sie rechts ab.")
    G.add_edge("F4.20_c", "F4.20_conn", weight=3, description="F4.20_c to F4.20_conn.")

    G.add_edge("F4.20_c", "toilet", weight=2, description="Gehen Sie den Korridor geradeaus weiter entlang, öffnen Sie die Tür vor Ihnen, biegen Sie gleich nach rechts ab und machen Sie 2 Schritte. Öffnen Sie die Tür und Sie erreichen die Toilette.")
    G.add_edge("toilet", "F4.20_c", weight=2, description="Öffnen Sie die Tür der Toilette, machen Sie 2 Schritte geradaus, biegen Sie nach links ab. Öffnen Sie die Tür vor Ihnen und gehen Sie geradeaus.")

    G.add_edge("toilet", "stairs-middle", weight=4, description="Öffnen Sie die Toilettentür, machen Sie 2 Schritte geradaus, biegen Sie nach rechts ab und machen Sie 2 Schritte geradeaus. Biegen Sie nach links ab und Sie erreichen die Stiegen des 4.Stocks.")
    G.add_edge("stairs-middle", "toilet", weight=4, description="Nachdem Sie den 4.Stock erreicht haben, gehen Sie geradeaus, indem Sie 2 Schritte machen und nach recht abbiegen. Danach machen Sie 2 Schritte geradeaus und biegen Sie demnächst nach links ab. Öffnen Sie die Tür vor Ihnen und Sie erreichen die Toilette.")

    G.add_edge("toilet", "lift", weight=4, description="Öffnen Sie die Toilettentür, machen Sie 2 Schritte geradaus, biegen Sie nach rechts ab und machen Sie 2 Schritte geradeaus. Biegen Sie nach rechts ab und Sie erreichen die Lifte.")
    G.add_edge("lift", "toilet", weight=4, description="Verlassen Sie den Lift, indem Sie 2 Schritte geradeaus machen und nach limks abbiegen. Danach machen Sie 2 Schritte geradeaus und biegen Sie demnächst nach links ab. Öffnen Sie die Tür vor Ihnen und Sie erreichen die Toilette.")

    G.add_edge("F4.20_c", "lift", weight=8, description="Gehen Sie den Korridor geradeaus weiter entlang, öffnen Sie die Tür vor Ihnen und machen Sie 5 Schritte geradeaus. Danach biegen Sie nach rechts ab, machen Sie 2 Schritte und Sie erreichen die 4 Lifte.")
    G.add_edge("lift", "F4.20_c", weight=8, description="Verlassen Sie den Lift, indem Sie 2 Schritte geradeaus machen. Danach biegen Sie nach links ab und gehen Sie geradeaus bis Sie die Tür vor Ihnen öffnen und nochmals 2 Schritte machen.")

    G.add_edge("lift", "stairs-middle", weight=2, description="Öffnen Sie die Toilettentür, machen Sie 2 Schritte geradaus und Sie erreichen die Stiegen des 4.Stocks.")
    G.add_edge("stairs-middle", "lift", weight=2, description="Nachdem Sie den 4.Stock erreicht haben, gehen Sie geradeaus, indem Sie 2 Schritte machen. Öffnen Sie die Tür vor Ihnen und Sie erreichen die Toilette.")

    G.add_edge("F4.01_F4.08_c", "stairs_middle", weight=9, description="Gehen Sie den Korridor 2 Schritte geradeaus weiter und sie erreichen die Tür, die in die Halle des 4.Stocks führt. Gehen Sie 5 Schritte geradeaus und biegen Sie nach rechts ab. Gehen Sie noch 2 Schritte nach vorne und Sie erreichen die Stiegen.")
    G.add_edge("stairs_middle", "F4.01_F4.08_c", weight=9, description="Nachdem Sie die 4.Etage erreicht haben, gehen Sie 2 Schritte geradeaus und biegen Sie demnächt nach links ab. Gehen Sie geradeaus weiter, bis sie die Türe vor ihnen erreichen, diese öffnen und noch 2 Schritte geradeaus machen.")

    G.add_edge("door_right", "toilets", weight=9, description="door_right to toilet.")
    G.add_edge("toilets", "door_right", weight=9, description="toilet to door_right.")

    G.add_edge("door_right", "lift", weight=6, description="door_right to lift.")
    G.add_edge("lift", "door_right", weight=6, description="lift to door_right.")

    G.add_edge("F4.01_F4.08_c", "F4.02_F4.07_c", weight=3, description="Gehen Sie den Korridor 2 Schritte geradeaus weiter.")
    G.add_edge("F4.02_F4.07_c", "F4.01_F4.08_c", weight=3, description="Gehen Sie den Korridor 2 Schritte geradeaus weiter.")

    G.add_edge("F4.01_F4.08_c", "door_right", weight=3, description="Gehen Sie den Korridor 2 Schritte geradeaus weiter bis Sie die Tür erreichen.")
    G.add_edge("door_right", "F4.01_F4.08_c", weight=3, description="Öffnen Sie die Tür, gehen Sie den Korridor 2 Schritte geradeaus weiter.")

    G.add_edge("door_left", "door_right", weight=10, description="Door left to Door right.")
    G.add_edge("door_right", "door_left", weight=10, description="Door right to Door left.")

    G.add_edge("door_left", "F4.20_c", weight=1, description="Door left to F4.20_c.")
    G.add_edge("F4.20_c", "door_left", weight=10, description="F4.20_c to Door left.")

    G.add_edge("F4.02_F4.07_c", "F4.03_F4.06_c", weight=3, description="Gehen Sie den Korridor 2 Schritte geradeaus weiter entlang.")
    G.add_edge("F4.03_F4.06_c", "F4.02_F4.07_c", weight=3, description="Gehen Sie den Korridor 2 Schritte geradeaus weiter entlang.")

    G.add_edge("F4.03_F4.06_c", "F4.04_F4.05_c", weight=3, description="Gehen Sie den Korridor 2 Schritte geradeaus weiter entlang.")
    G.add_edge("F4.04_F4.05_c", "F4.03_F4.06_c", weight=3, description="Gehen Sie den Korridor 2 Schritte geradeaus weiter entlang.")

    G.add_edge("F4.04_F4.05_c", "stairs_right_conn", weight=2, description="Gehen Sie im Korridor zwei Schritte geradeaus. Sie werden eine Wand spüren, an der Sie sich orientieren können.")
    G.add_edge("stairs_right_conn", "F4.04_F4.05_c", weight=2, description="Gehen Sie im Korridor zwei Schritte geradeaus.")

    G.add_edge("stairs_right_conn", "stairs_right", weight=6, description="Gehen Sie den Korridor 6 Schritte geradeaus weiter entlang, bis Sie das Ende des Korridors erreichen. Hier finden Sie eine Tür auf Ihrer rechten Seite. Fühlen Sie nach dem Türgriff, um die Tür zu öffnen und die Stiegen zu erreichen.")
    G.add_edge("stairs_right", "stairs_right_conn", weight=6, description="Öffnen Sie die Tür vor Ihnen, um in den Korridor der 4. Etage zu gelangen, und biegen Sie unmittelbar links ab. Gehen Sie den Korridor 6 Schritte geradeaus weiter, bis Sie spüren, dass die Wand auf Ihrer linken Seite endet. Dies zeigt das Auftreten eines neuen Korridors auf Ihrer rechten Seite an.")

    return G

# Calculate turn direction based on the angles of two consecutive edges
def calculate_turn_direction(angle1, angle2):
    # Calculate the difference in angle
    print(f"angle1: {angle1}, angle2: {angle2}")
    angle_diff = angle2 - angle1
    # Normalize the angle difference
    angle_diff = (angle_diff + 180) % 360 - 180  # Angle difference in range [-180, 180]
    print(f"angle_diff: {angle_diff}")

    if angle1 == 0 or angle2 == 0:
        print("description not appended, one of the angles = 0")
        return None
    elif angle_diff == 90:
        print("description 'links' appended")
        return 'links'
    elif angle_diff == -90:
        print("description 'rechts' appended")
        return 'rechts'
    else:
        print("turn description not appended, angle difference does not equal +/-90")
        return None


def calculate_angles(graph, prev_node, current_node, next_node):
    node_data1 = graph.nodes[prev_node] if prev_node else graph.nodes[current_node]
    node_data2 = graph.nodes[current_node]
    node_data3 = graph.nodes[next_node] if next_node else None

    coord1 = node_data1.get('coord') 
    coord2 = node_data2.get('coord')
    coord3 = node_data3.get('coord') if node_data3 else None

    if not coord3:
        return ''

    print(f"coord1: {coord1}, coord2: {coord2}, coord3: {coord3}")
    
    # Calculate the vectors for the incoming and outgoing paths
    vector_in = (coord2[0] - coord1[0], coord2[1] - coord1[1])
    vector_out = (coord3[0] - coord2[0], coord3[1] - coord2[1])
    
    # Calculate the angle between vectors
    angle_in = math.atan2(vector_in[1], vector_in[0])
    angle_out = math.atan2(vector_out[1], vector_out[0])
    
    # Use the angles to determine the direction
    return calculate_turn_direction(math.degrees(angle_in), math.degrees(angle_out))


def find_shortest_path(graph, start_node, end_node):
    try:
        path = nx.dijkstra_path(graph, start_node, end_node)
        path_edges = [(path[n], path[n + 1]) for n in range(len(path) - 1)]
        descriptions = []
        accumulated_distance = 0
        accumulated_nodes = 0

        for i, edge in enumerate(path_edges):
            current_node, next_node = edge
            current_index = path.index(current_node)
            prev_node = path[i - 1] if i > 0 else current_node
            edge_data = graph[current_node][next_node]
            print(prev_node + " - " + str(graph.nodes[prev_node]['coord']))
            print(current_node + " - " + str(graph.nodes[current_node]['coord']))
            print(next_node + " - " + str(graph.nodes[next_node]['coord']))
            print(edge_data)
            print("BREAK")

            turn = calculate_angles(graph, prev_node, current_node, next_node)

            if (graph.nodes[current_node]['type'] == 'corridor' and graph.nodes[next_node]['type'] == 'corridor' or 
                graph.nodes[current_node]['type'] == 'conn' and graph.nodes[next_node]['type'] == 'corridor'):
                print("Condition for skipping edges is met")
                # Accumulate distance
                accumulated_distance += edge_data['weight']
                accumulated_nodes += 1
                
                if turn:
                    descriptions.append(f"Biegen Sie {turn} ab. ")

            else:
                # Add accumulated distance to the description
                if accumulated_distance:
                    print("Finally appending the entire corridor description")
                    descriptions.append(f"Gehen Sie geradeaus {accumulated_distance} Schritte im Korridor, vorbei an {accumulated_nodes} Zimmern")
                    accumulated_distance = 0
                    accumulated_nodes = 0

                if turn:
                    descriptions.append(f"Biegen Sie {turn} ab. ")
        
                # If there is no accumulated distance, add the current edge's description
                print("Simply appending edge description")
                descriptions.append(edge_data['description'])

            print(descriptions)
        
        return path, descriptions
    
    except nx.NetworkXNoPath:
        return None, "No path exists between the specified nodes."