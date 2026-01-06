import json
from datetime import datetime
from pathlib import Path

HISTORY_FILE = Path("history.json")

def save_history(action, algorithm, result):
    entry = {
        "action": action,
        "algorithm": algorithm,
        "result": result,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if HISTORY_FILE.exists():
        data = json.loads(HISTORY_FILE.read_text())
    else:
        data = []

    data.append(entry)
    HISTORY_FILE.write_text(json.dumps(data, indent=4))

def load_history():
    if not HISTORY_FILE.exists():
        return []
    return json.loads(HISTORY_FILE.read_text())

def clear_history():
    if HISTORY_FILE.exists():
        HISTORY_FILE.unlink()
