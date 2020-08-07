#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # build hash table with source: destination
    table = {}
    for t in tickets:
        table[t.source] = t.destination

    # reconstruct route
    route = [table["NONE"]]
    while route[-1] != "NONE":
        route.append(table[route[-1]])

    return route
