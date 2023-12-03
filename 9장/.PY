def search_max_bst(n):
    if n is None or n.right is None:
        return n
    return search_max_bst(n.right)


def search_min_bst(n):
    if n is None or n.left is None:
        return n
    return search_min_bst(n.left)
