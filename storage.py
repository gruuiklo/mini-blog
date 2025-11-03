from pathlib import Path

DATA_FILE = Path("data/posts.txt")

def save_post(text):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\\n")

def load_posts():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return f.readlines()
