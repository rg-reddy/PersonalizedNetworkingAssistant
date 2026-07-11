import json
import os

FEEDBACK_FILE = "data/feedback.json"

def load_feedback():
    if not os.path.exists(FEEDBACK_FILE):
        return []

    try:
        with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def save_feedback(entry):
    feedback = load_feedback()
    feedback.append(entry)

    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        json.dump(feedback, f, indent=4)