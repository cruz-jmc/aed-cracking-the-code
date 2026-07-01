def bfs(tree):
    if not tree.get_root():
        return []

    # Usamos uma lista normal do Python como fila
    fila = [tree.get_root()]
    visit_order = []

    # Enquanto a fila não estiver vazia
    while fila:
        # Pega e remove o primeiro elemento da fila (índice 0)
        node = fila.pop(0)
        visit_order.append(node)

        # Se tiver filho esquerdo, adiciona no fim da fila
        if node.has_left_child():
            fila.append(node.get_left_child())

        # Se tiver filho direito, adiciona no fim da fila
        if node.has_right_child():
            fila.append(node.get_right_child())

    return visit_order