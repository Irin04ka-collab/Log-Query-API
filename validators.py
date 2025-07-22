import os

from flask import abort

from config import DATA_DIR, ARGS


def validate_args(request_args: dict):
    if set(request_args.keys()) != ARGS:
        abort(400, description="Error of request")

def validate_file_exists(file_name):
    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.isfile(file_path):
        abort(400, description=f"The file {file_name} not exits in {DATA_DIR}")

