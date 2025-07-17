

# my idea: if list[][1] exists count+ and coninue

'''
def count_layers(sandwich):
    # isinstance(sandwich, list)
    max_layer = 0
    for cur_item in sandwich:
        if isinstance(cur_item, list):
            layer_count = count_layers(cur_item)
            max_layer = max(layer_count, max_layer)

    return max_layer + 1
'''