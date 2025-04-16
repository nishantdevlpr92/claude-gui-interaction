# Project Setup Guide

## Prerequisites
Make sure you have the following installed on your system:
- **Python 3.10**
- **Git**
- **virtualenv** (Python virtual environment tool)

To install `virtualenv` on linux, run: 
```sh
sudo apt install python3.10-venv
```

---

## Backend Setup (Flask)

### 1. Clone the Project
Open a terminal and run:
Clone the repository:
```sh
git clone https://github.com/username/repo.git
cd claude-gui-interaction
```

### 2. Set Up the Backend
Create and activate a virtual environment using `virtualenv`:
```sh
python -m venv env
source env/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

Install dependencies:
```sh
pip install -r requirements.txt
```


### 6. Start the Backend Server
```sh
python3 app.py
```

### 7. Run GUI Interaction Script (mouse_demo.py)
#### 1. Open a new terminal window
#### 2. Navigate to project directory:
```sh
cd claude-gui-interaction
```
#### 3. Activate the virtual environment:
```sh
source env/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```
#### 4. Run Script:
```sh
python3 mouse_demo.py
```