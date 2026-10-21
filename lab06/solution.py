# def count_items(values):
#     counts = {}
#     for items in values:
#         counts[items] = counts.get(items, 0) + 1
#     return counts
 
# def unique_sorted(values):
#     return sorted(set(values), key=True)

def common(first, second):
    c = set(first) & set(second)
    return sorted(c)

def only_in_first(first, second):
    c = set(first) - set(second)
    return sorted(c)


