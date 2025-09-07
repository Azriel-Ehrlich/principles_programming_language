
def add_3_dicts(d1, d2, d3):
    """ Return a dictionary that contains all keys from d1, d2, and d3.
        The value for each key is a set of all values associated with that key
        in the input dictionaries. If a key is missing in a dictionary,
        it does not contribute to the set of values for that key.
    """
    def values_for_key(k):
        """ Return a tuple of all values for key k from d1, d2, and d3 without duplicates. """
        values = filter(lambda x: x is not None,
                       map(lambda d: d.get(k), [d1, d2, d3]))
        return tuple(dict.fromkeys(values))
    # get all unique keys from the three dictionaries
    all_keys = set(d1) | set(d2) | set(d3)
    # create a new dictionary with keys and their corresponding sets of values
    return dict(map(lambda k: (k, values_for_key(k)), all_keys))

# example
d1 = {'a': 1, 'b': 2}
d2 = {'b': 2, 'c': 4}
d3 = {'c': 5, 'd': 6}
result = add_3_dicts(d1, d2, d3)
print(result)  