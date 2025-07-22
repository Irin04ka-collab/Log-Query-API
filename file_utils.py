
def load_file_lines(file_path):
    with open(file_path) as f:
        for line in f:
            yield line



