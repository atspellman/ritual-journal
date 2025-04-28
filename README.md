# 🕯️ The Ritual Journal

*A ritual-themed command-line journal for developers, dreamers, and the digitally devoted.*

---

**The Ritual Journal** is a Python-based CLI journaling system that stores your daily rituals, reflections, or dream fragments in a flat file. Designed for terminal-based practice and personal myth-building, it turns ordinary logs into sacred text.

---

## ✨ Features

- 📓 Record ritual entries with:
  - Ritual name
  - Notes or offerings (optional)
  - Category (e.g., code, bug, dream, reflection)
  - Tags (comma-separated)
  - Mood sigil (emoji or symbol)

- 🔍 Filter entries by keyword or date
- 📖 Scroll entries page by page inside the terminal
- 🎨 Colored output (via `colorama`) for easier reading
- 🔥 Entries are stored in a ledger file / sqlite 
- 🧙🏻 Thematic language and immersive prompts

---

## 📂 File Structure

ritual/

├── .venv/             # Virtual environment (ignored by Git)

├── ledger.txt         # The sacred record of your entries (ignored by Git)

├── ritual-journal.py          # Main script (The Watcher's heart)

├── .gitignore         # Keeps ledger.txt and .venv from being tracked

└── README.md          # This very file

---

## 🧙 Command Menu

1 – Record a new ritual  
2 – Read the Ledger (with filters and pagination)  
3 – Exit the sanctum

---

## 🪬 Roadmap
- [x] Flat file ledger <code>(ledger.txt)</code>
- [x] Terminal color output using <code>colorama</code>
- [x] Pagination for navigating long logs
- [x] Tag-based filtering
- [ ] Export entries to Markdown or plain text
- [ ] Entry editing or deletion
- [ ] Add "ritual streaks" or calendar view
- [ ] Encrypt ledger or password protection

---

## 🚀 Setup & Usage
### 1. Clone the repo
  git clone https://github.com/atspellman/Ritual-Journal.git

  cd Ritual-Journal

---

### 2.Create a virtual environment
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

---

### 3. Run the script
python ritual-journal.py

---

## 🧾 License

Open source and available under the MIT License.
