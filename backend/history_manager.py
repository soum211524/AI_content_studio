import json
from datetime import datetime

HISTORY_FILE = "storage/history.json"


def save_history(data):

    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    except:
        history = []

    data["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    history.append(data)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


def get_history():

    try:
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    except:
        history = []

    return history[::-1]