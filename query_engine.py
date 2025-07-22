# apply_query(lines, query) — реализовать через map / filter
# и термы запроса (filter, map, unique, limit, sort, и т.п.)
from flask import abort


def apply_query(lines, query, value):
    if query == "filter":
        result = list(filter(lambda line: value in line, lines))

    elif query == "map":
        ind = int(value)
        result = list(map(lambda line: line.split(" ")[ind], lines))

    elif query == "sort":
        if value == "asc":
            result = sorted(lines, reverse=False)
        elif value == "desc":
            result = sorted(lines, reverse=True)
        else:
            abort(400, description="The value of sort is not expected")

    elif query == "limit":
        list_of_limit = range(int(value))
        zipped = zip(lines, list_of_limit)
        result, list_of_limit = zip(*zipped)

    elif query == "unique":
        result = dict.fromkeys(lines)

    else:
        abort(400, description="Error of cmd")
    return result
