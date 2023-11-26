# 20

def level(root, node):
    level = 0
    queue = [(root, 0)]
    while queue:
        current, level = queue.pop(0)
        if current is None:
            continue
        if current.data == node:
            return level
        queue.append((current.left, level + 1))
        queue.append((current.right, level + 1))
    return 0
