from data_structures.node import Node


def tree_height(root: Node | None) -> int:
    if root is None: # caso base: árvore vazia tem altura -1
        return -1

    left_height = tree_height(root.left) # altura da subárvore esquerda
    right_height = tree_height(root.right) # altura da subárvore direita

    return max(left_height, right_height) + 1 # a altura da árvore é a maior altura das 
    # subárvores (direita e esquesda) + 1 para contar o nó atual.