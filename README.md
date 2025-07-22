# Log Query API

This project implements a simple Flask-based API that allows users to perform queries on a log file using functional programming techniques. It supports filtering and transforming log lines using specified commands.

## Features

- API endpoint to process log queries via POST requests.
- Input validation and error handling (400 errors for invalid requests).
- Functional-style processing with `filter`, `map`, and generators.
- Supports chaining of two commands per request.
- Reads log data from a file stored in a configurable directory.

## Technologies

- Python 3.x
- Flask
- Functional programming tools (`filter`, `map`)
- Standard library modules: `os`, `json`, `typing`


## API Usage

### Endpoint

POST /perform_query

### Supported Commands

| Command | Description                              |
|---------|------------------------------------------|
| filter  | Filters lines that contain a substring   |
| map     | Selects column by index (0-based)        |
| unique  | Returns only unique lines                |
| sort    | Sorts the lines alphabetically           |
| limit   | Limits the number of output lines        |


### Request Body (JSON)

```json
{
  "file_name": "apache_logs.txt",
  "cmd1": "filter",
  "value1": "GET",
  "cmd2": "map",
  "value2": "0"
}


