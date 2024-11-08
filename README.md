# JSON to ENV Converter

A Debian package that provides a command-line tool to convert JSON file into single environment variable string.

## Installation

### Building from source

```bash
# Install build dependencies
sudo apt-get install build-essential dh-python python3-all python3-setuptools

# Clone the repository
git clone https://github.com/HeinSoeHtet/json_to_env.git
cd json_to_env

# Build the package
python3 setup.py --command-packages=stdeb.command bdist_deb

# Install the generated .deb package.
sudo dpkg -i deb_dist/python3-json-to-env_1.0.0-1_all.deb
```

## Usage

Basic usage:

```bash
json_to_env example_input.json
```

Test:

```bash
python3 -m unittest discover -s test -p "test_*.py"
```

## Package Details

- Package: json_to_env
- Version: 1.0
- Architecture: all
- Maintainer: DevHein <cantatasonatadev@gmail.com>
- Description: Convert JSON files to environment variable format
- Dependencies: python3

## Files Installed

- `/usr/bin/json_to_env` - Main executable
- `/usr/lib/python3/dist-packages/json_to_env.py` - Python module

## System Requirements

- Debian-based Linux distribution (Debian, Ubuntu, etc.)
- Python 3.x

## License

This package is licensed under the MIT License.

## Support

For bug reports and feature requests, please visit:
https://github.com/HeinSoeHtet/json_to_env/issues

## Author

DevHein <cantatasonatadev@gmail.com>
