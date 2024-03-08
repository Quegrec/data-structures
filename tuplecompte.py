def tuplecount(lst):
    max_tuple = ()
    max_count = 0
    for item in lst:
        if isinstance(item, tuple) and len(item) > max_count:
            max_tuple = item
            max_count = len(item)
    return max_tuple
