import json
import sys


def json_to_env(json_file):
    try:
        with open(json_file, "r") as f:
            data = json.load(f)

        if not isinstance(data, (dict, list)):
            raise ValueError("JSON content is neither a dictionary nor an array")

        # Convert the JSON data to a compact single-line JSON string
        json_string = json.dumps(data, separators=(",", ":"))
        print(json_string)
    except json.JSONDecodeError:
        print(
            f"Error: The file '{json_file}' is not a valid JSON file.", file=sys.stderr
        )
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)


def main():
    if len(sys.argv) != 2:
        print("Usage: json_to_env <json_file>")
        sys.exit(1)
    json_file = sys.argv[1]
    json_to_env(json_file)
