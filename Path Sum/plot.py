import igraph


def plot_binary_tree(list_of_nodes: []):
    if len(list_of_nodes) == 0:
        return None

    named_nodes = [(str(node_id), value) for node_id, value in enumerate(list_of_nodes)]
    g = igraph.Graph()

    root_id, root_val = named_nodes.pop(0)
    queue = [root_id]
    g.add_vertex(name=root_id, val=root_val)

    while named_nodes:
        current_id = queue.pop(0)
        left_id, left_val = named_nodes.pop(0)
        right_id, right_val = named_nodes.pop(0)
        if left_val:
            g.add_vertex(name=left_id, val=left_val)
            g.add_edge(current_id, left_id)
            queue.append(left_id)
        if right_val:
            g.add_vertex(name=right_id, val=right_val)
            g.add_edge(current_id, right_id)
            queue.append(right_id)

    layout = g.layout_reingold_tilford(root=[0])
    g.vs['label'] = g.vs['val']
    igraph.plot(g, layout=layout)
