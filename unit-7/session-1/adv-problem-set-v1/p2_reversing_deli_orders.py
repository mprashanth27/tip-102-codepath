'''
def reverse_orders(orders):
    if not orders or " " not in orders:
        return orders

    first_space = orders.find(" ")
    first_order = orders[:first_space]
    remaining_orders = orders[first_space + 1 :]

    reversed_remaining = reverse_orders(remaining_orders)

    return reversed_remaining + " " + first_order


# print(reverse_orders("Bagel Sandwich Coffee"))
'''