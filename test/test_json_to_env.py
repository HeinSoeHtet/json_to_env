import unittest
import json
from unittest.mock import patch
from io import StringIO
import json_to_env


class TestJsonToEnv(unittest.TestCase):

    def test_json_to_env_valid_json(self):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            json_to_env.json_to_env("test_data/valid.json")
            self.assertEqual(
                mock_stdout.getvalue().strip(),
                '{"name":"John","age":30,"city":"New York"}',
            )

    def test_json_to_env_invalid_json(self):
        with patch("sys.stderr", new_callable=StringIO) as mock_stderr:
            json_to_env.json_to_env("test_data/invalid.json")
            self.assertIn(
                "Error: The file 'test_data/invalid.json' is not a valid JSON file.",
                mock_stderr.getvalue(),
            )

    def test_json_to_env_not_a_dictionary_or_list(self):
        with patch("sys.stderr", new_callable=StringIO) as mock_stderr:
            json_to_env.json_to_env("test_data/not_a_dictionary_or_list.json")
            self.assertIn(
                "Error: JSON content is neither a dictionary nor an array",
                mock_stderr.getvalue(),
            )

    def test_main_valid_json(self):
        with patch("sys.argv", ["json_to_env", "test_data/valid.json"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                json_to_env.main()
                self.assertEqual(
                    mock_stdout.getvalue().strip(),
                    '{"name":"John","age":30,"city":"New York"}',
                )

    def test_main_no_file_argument(self):
        with patch("sys.argv", ["json_to_env"]):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                with self.assertRaises(SystemExit) as context:
                    json_to_env.main()
                self.assertEqual(context.exception.code, 1)
                self.assertEqual(
                    mock_stdout.getvalue().strip(), "Usage: json_to_env <json_file>"
                )
