def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Add all items to a hash table with weight: index
    table = {}
    for i in range(len(weights)):
        # store indices in arrays so that we can handle duplicate weights
        if weights[i] in table:
            table[weights[i]].append(i)
        else:
            table[weights[i]] = [i]

    # Check each item to see if there is a matching weight
    # (i is descending so that we get the highest index solution possible)
    for i in range(len(weights)-1, -1, -1):
        w = limit - weights[i]  # matching weight
        if w in table:
            # found a match
            if len(table[w]) == 1:
                # only 1 item with that weight
                return (i, table[w][0])
            else:
                # multiple items, find highest matching index that isn't i
                idx = table[w][0]
                for j in table[w]:
                    if j > idx and j != i:
                        idx = j
                return (i, idx)

    # No match found, return None
    return None
