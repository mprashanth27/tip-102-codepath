from unit_8.binary_tree import TreeNode

def merge_orders(order1, order2):
    if not order1:
        return order2
    if not order2:
        return order1

    newGrootsum = TreeNode(order1.val + order2.val)

    newGrootsum.left = merge_orders(order1.left, order2.left)
    newGrootsum.right = merge_orders(order1.right, order2.right)

    return newGrootsum