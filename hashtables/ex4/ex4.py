def has_negatives(a):
    """
    YOUR CODE HERE
    """
    table = {}
    result = []
    for n in a:
        # See if we have already found the negative of this number
        if -n in table:
            result.append(abs(n))

        # Add this number to the table
        table[n] = None

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
