def em_ordem (tree):
    if not tree.get_root():
        return []

    visit_order = []

    def traverse(node):
        if node:
            traverse(node.get_left_child())  # Visita o filho esquerdo
            visit_order.append(node)  # Visita o nó atual
            traverse(node.get_right_child())  # Visita o filho direito

    traverse(tree.get_root())
    return visit_order