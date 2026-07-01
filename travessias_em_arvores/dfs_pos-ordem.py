def pos_ordem (tree):
    if not tree.get_root():
        return []

    visit_order = []

    def traverse(node):
        if node:
            traverse(node.get_left_child())  # Visita o filho esquerdo
            traverse(node.get_right_child())  # Visita o filho direito
            visit_order.append(node)  # Visita o nó atual

    traverse(tree.get_root())
    return visit_order