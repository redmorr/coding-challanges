import igraph
from node import Node


def plot_binary_tree(root: Node):
    if not root:
        return None

    graph = igraph.Graph()
    graph.add_vertex(name=root.id, val=root.val)

    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
            graph.add_vertex(name=node.left.id, val=node.left.val)
            graph.add_edge(source=node.id, target=node.left.id)
        if node.right:
            queue.append(node.right)
            graph.add_vertex(name=node.right.id, val=node.right.val)
            graph.add_edge(source=node.id, target=node.right.id)

    layout = graph.layout_reingold_tilford(root=[0])
    graph.vs['label'] = graph.vs['val']
    igraph.plot(graph, layout=layout)
