from data_structures.node import Node


def lowest_common_ancestor(
    root: Node | None,
    value1: int,
    value2: int,
) -> int:
    if root is None:
        return -1 # Retorna -1 para indicar que nenhum dos valores foi encontrado nesta subárvore.

    if root.value == value1 or root.value == value2:
        return root.value # Retorna o valor do nó atual se ele for igual a value1 ou value2

    left_lca = lowest_common_ancestor(root.left, value1, value2) # Busca recursivamente na 
    # subárvore esquerda
    right_lca = lowest_common_ancestor(root.right, value1, value2) # Busca recursivamente na 
    # subárvore direita

    if left_lca != -1 and right_lca != -1:
        return root.value # Se ambos os lados retornarem um valor diferente de -1, significa que 
        # encontramos ambos os valores em subárvores diferentes, então o nó atual é o LCA.

    return left_lca if left_lca != -1 else right_lca # Retorna o valor encontrado em um dos lados,
    # ou -1 se nenhum dos valores foi encontrado em ambas as subárvores.