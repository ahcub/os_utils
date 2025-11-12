Utils for python
====================

os utils for python to reduce copy-pasting same functionality and unity functions to handle common problems with delete of file or directory or creating directory
- logging configuration
- path operations (delete, creating)
- files operation (like md5 calculation or zipping a folder)

## Installation

This project uses [uv](https://docs.astral.sh/uv/) as the package manager.

### Install uv

```bash
# On macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Install the package

```bash
# Install from PyPI
uv pip install os_utils

# Or install in development mode
uv pip install -e .
```

## Development

```bash
# Sync dependencies
uv sync

# Run Python with uv
uv run python your_script.py
```