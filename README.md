# Calculator App — Python + Flask
 
A calculator built in two parts:
- **Python CLI App** — runs in your terminal
- **Web App** — Flask backend + HTML/CSS/JS frontend

---

## Project Structure 
 
```
calculator_app/
├── python_app/
│   ├── calculator.py   # Core calculator logic (reusable class)
│   └── main.py         # Command-line interface
├── web_app/
│   ├── app.py          # Flask backend (reuses calculator.py) 
│   ├── templates/
│   │   └── index.html  # Web UI
│   └── static/
│       ├── css/style.css
│       └── js/app.js
├── requirements.txt
└── README.md
```

---

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Python CLI

```bash
cd python_app
python main.py
```

Follow the on-screen menu to perform calculations.

### 3. Run the Web App

```bash
cd web_app
python app.py
```

Then open your browser at: **http://localhost:5000**

---

## Features

| Feature        | CLI | Web |
|----------------|-----|-----|
| Add            | ✅  | ✅  |
| Subtract       | ✅  | ✅  |
| Multiply       | ✅  | ✅  |
| Divide         | ✅  | ✅  |
| Power (a^b)    | ✅  | ✅  |
| Modulo (a%b)   | ✅  | ✅  |
| History        | ✅  | ✅  |
| Clear History  | ✅  | ✅  |
| Division by 0  | ✅  | ✅  |

---

## Requirements

- Python 3.8+
- Flask 3.x (for the web app only)
