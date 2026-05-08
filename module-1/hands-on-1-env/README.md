# Hands-on 1: Setting up the development environment

## Goal
Get your laptop ready for Python development.

## What you will do
- Confirm Python is installed
- Create a workspace folder for this module
- Verify you can run Python and `pip`

## Steps

### 1) Verify Python
Run:

```bash
python3 --version
```

**If `python3` is not found:**
- **Linux (Ubuntu/Debian):** `sudo apt update && sudo apt install python3`
- **macOS:** `brew install python` (requires Homebrew)
- **Windows:** Download from [python.org](https://www.python.org/downloads/) and ensure "Add Python to PATH" is checked.

### 2) Verify pip
Pip is the package installer for Python. Run:

```bash
python3 -m pip --version
```

**If `pip` is not found:**
- **Linux:** `sudo apt install python3-pip`
- **macOS/Windows:** It usually comes with Python. If missing, run `python3 -m ensurepip --upgrade`.

### 3) Create a working folder
Navigate to your preferred projects directory and create a workspace:

```bash
# Example for Linux/macOS
mkdir -p ~/aiops-practice/module-1
cd ~/aiops-practice/module-1
```

## Practical exercise
- Create a file named `sanity_check.py` with this content:

```python
import sys
print("python:", sys.version)
```

- Run it:

```bash
python3 sanity_check.py
```

## Expected output
You should see a Python version string printed.
