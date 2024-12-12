# Keyboard Script

This script periodically types a predefined message and sends a notification when the 'Esc' key is pressed to exit the script.

## Features

- Types a predefined message at regular intervals.
- Sends a notification when the 'Esc' key is pressed to exit the script.

## Requirements

- Python 3.x
- `pyautogui`
- `keyboard`
- `plyer`

## Setup

### Create a Virtual Environment

It is recommended to create a virtual environment for better dependency management. Follow these steps to set up the virtual environment and install the required packages:

1. **Create a virtual environment**:

```sh
python -m venv venv
```

2. **Activate the virtual environment**:

On Windows:

```sh
.\venv\Scripts\activate
```

On macOS/Linux:

```sh
source venv/bin/activate
```

3. **Install the required packages**:

```sh
pip install pyautogui keyboard plyer
```

### Run the Script

After setting up the virtual environment and installing the required packages, you can run the script:

```sh
python script_name.py
```

### Usage

- The script will type the predefined message at regular intervals.
- Press and hold the 'Esc' key to exit the script and receive a notification.

### Executable

An executable version of the script is also available for use. You can run the executable without setting up a Python environment. If you encounter any issues with your antivirus software, you may need to temporarily disable it to run the executable.
