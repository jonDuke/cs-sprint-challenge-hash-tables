def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Build a table with file: path
    table = {}
    for path in files:
        f = path.split('/')[-1]  # extract filename

        # add to the table
        if f in table:
            table[f].append(path)
        else:
            table[f] = [path]

    result = []
    for f in queries:
        # append all paths for each queried file
        if f in table:
            result.extend(table[f])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
