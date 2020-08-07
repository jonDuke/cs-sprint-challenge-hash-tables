def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Add items from first list into the table
    table = {}
    for n in arrays[0]:
        table[n] = False

    # For each other list...
    for i in range(1, len(arrays)):
        # Change each item found to True
        for n in arrays[i]:
            if n in table:
                table[n] = True

        # Delete any False items (were not found)
        # Change everything back to False for next loop
        keys = list(table.keys())  # copy keys to separate list so we can safely delete some
        for key in keys:
            if table[key]:
                table[key] = False
            else:
                del(table[key])

    # Remaining keys are the common elements
    return list(table.keys())


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
