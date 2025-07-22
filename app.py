import os

from flask import Flask, request, abort

from config import DATA_DIR
from file_utils import load_file_lines
from query_engine import apply_query
from validators import validate_args

app = Flask(__name__)


@app.route("/perform_query", methods=['POST'])
def perform_query():
    # Get 'query' and 'file_name' from request.args, return 400 on error
    payload = request.get_json()
    validate_args(request.get_json())

    # Check if the file exists in DATA_DIR, return 400 if not found
    file_path = os.path.join(DATA_DIR, payload["file_name"])
    if not os.path.isfile(file_path):
        abort(400, description=f'The file {payload["file_name"]} not exits in {DATA_DIR}')

    # Use functional programming (filter, map) and iterators/generators to build the query
    lines = load_file_lines(file_path)

    res = apply_query(lines, payload["cmd1"], payload["value1"])
    result = apply_query(res, payload["cmd2"], payload["value2"])

    # Return the final result to the user
    return "\n".join(result)

if __name__ == '__main__':
    app.run(debug=True)
