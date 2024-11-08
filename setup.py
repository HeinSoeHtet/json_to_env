from setuptools import setup, find_packages

setup(
    name="json_to_env",
    version="1.0.0",  # Using semantic versioning x.y.z
    description="A tool to convert JSON files to a single environment variable string",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="devhein",
    author_email="cantatasonatadev@gmail.com",
    url="https://github.com/HeinSoeHtet/json_to_env",
    maintainer="devhein",
    maintainer_email="cantatasonatadev@gmail.com",
    license="MIT",
    packages=find_packages(),
    py_modules=["json_to_env"],
    python_requires=">=3.0",
    entry_points={
        "console_scripts": [
            "json_to_env=json_to_env:main",
        ],
    },
    keywords="json environment variables converter",
)
