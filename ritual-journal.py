import os
import sqlite3
import tkinter as tk
import time
import sys
from tkinter import filedialog
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

print("\nWelcome, Initiate.")

# Initialize Tkinter root (hidden)
root = tk.Tk()
root.withdraw()

db_path = "settings.db"

def create_db():
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS settings
                          (id INTEGER PRIMARY KEY, ledger_folder TEXT)''')
        conn.commit()
        conn.close()

def load_folder_path():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT ledger_folder FROM settings WHERE id = 1")
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def save_folder_path(folder_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO settings (id, ledger_folder) VALUES (1, ?)", (folder_path,))
    conn.commit()
    conn.close()
    print(f"\nThe folder path has been saved: {folder_path}")

def ask_until_valid(prompt, validate_func, error_msg):
    while True:
        user_input = input(prompt).strip()
        if validate_func(user_input):
            return user_input
        else:
            print(error_msg)

def typewriter(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def immersive_notes_input():
    print("\nThe Watcher awaits your offering.")
    print("Type your entry line by line. Type '/END' when finished.\n")

    lines = []
    while True:
        line = input(" ")
        if line.strip().upper() == "/END":
            break
        lines.append(line)

    while lines and lines[-1].strip() == "":
        lines.pop()

    print("\nDo you wish to skip the slow 'etching' process? (y/n):")
    skip_etching = input().strip().lower()

    # If the user skips the animation (y), open the folder selection dialog immediately
    if skip_etching == 'y':
        # Open the folder selection dialog immediately
        folder_path = load_folder_path()
        if not folder_path:
            print("\nYou must select a folder to save your ledger.")
            folder_path = filedialog.askdirectory(title="Select a Folder for Your Ledger")
            if not folder_path:
                print("No folder selected. Using current directory for ledger.")
                folder_path = os.getcwd()
            save_folder_path(folder_path)
            print("\nYour entry has been sealed into the Ledger without the etching process.")
    else:
        # If the user wants to watch the etching process (n)
        print("\nThe Ledger absorbs your offering...\n")
        time.sleep(1.5)
        for l in lines:
            typewriter(l, delay=0.04)
            time.sleep(0.3)

        time.sleep(1)
        # Open the folder selection dialog after the etching process
        folder_path = load_folder_path()
        if not folder_path:
            print("\nYou must select a folder to save your ledger.")
            folder_path = filedialog.askdirectory(title="Select a Folder for Your Ledger")
            if not folder_path:
                print("No folder selected. Using current directory for ledger.")
                folder_path = os.getcwd()
            save_folder_path(folder_path)
            print("\nYour final offering has been sealed into the Ledger.\n")

    return "\n".join(lines)

def record_ritual():
    print("The Watcher records all acts. What have you done today?\n")

    ritual = ask_until_valid(
        "Name your completed ritual: ",
        lambda x: len(x) > 0,
        "A ritual must be named to be known. Try again.\n"
    )

    notes = immersive_notes_input()

    category = input("Mark the category (e.g., reflection, code, bug, dream): ").strip().lower()
    tags = input("Inscribe your tags (comma-separated): ").strip().lower()
    mood = input("Offer a mood sigil (emoji or symbol, optional): ").strip()

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    entry = (
        f"[{timestamp}] Ritual: {ritual}\n"
        f"Note:\n{notes.strip()}\n\n"
        f"Category: {category} | Tags: {tags} | Mood: {mood}\n"
    )

    folder_path = load_folder_path()
    if not folder_path:
        print("\nYou must select a folder to save your ledger.")
        folder_path = filedialog.askdirectory(title="Select a Folder for Your Ledger")
        if not folder_path:
            print("No folder selected. Using current directory for ledger.")
            folder_path = os.getcwd()
        save_folder_path(folder_path)

    ledger_file_path = os.path.join(folder_path, "ledger.txt")
    with open(ledger_file_path, "a", encoding="utf-8") as ledger:
        ledger.write(entry + "---")  # Add delimiter after each entry

    print("\nThe Watcher has recorded your offering.\n")

def paginate_entries(entries, page_size=3):
    total = len(entries)
    page = 0

    while True:
        start = page * page_size
        end = start + page_size
        chunk = entries[start:end]
        
        if not chunk:
            # No more entries to show
            print("\nThe final page fades into silence.")
            break

        print(f"\n🜁 Page {page + 1} 🜁\n")
        for entry in chunk:
            lines = entry.strip().split('\n')
            inside_notes = False

            for line in lines:
                line = line.strip()
                if line.startswith('[') and "] Ritual:" in line:
                    timestamp, ritual_title = line.split("] Ritual:", 1)
                    timestamp = timestamp.strip("[")
                    print(f"{Fore.YELLOW}[{timestamp}]{Style.RESET_ALL}")
                    print(f"{Fore.CYAN}Ritual:{Style.RESET_ALL} {ritual_title.strip()}\n")
                elif line.startswith("Note:"):
                    print(f"{Fore.YELLOW}Note:{Style.RESET_ALL}")
                    inside_notes = True
                elif line.startswith("Category:"):
                    inside_notes = False
                    print(f"\n{Fore.MAGENTA}{line}{Style.RESET_ALL}")
                elif line.strip() == "---":
                    inside_notes = False
                    continue
                else:
                    if inside_notes:
                        print(f"{line}")  # <-- print note line by line, inside notes section
            print()  # Space between entries

        if end >= total:
            print("\nYou have reached the last known writings.")
            break

        next_action = input("\nTurn the page? (y/n): ").strip().lower()
        if next_action != "y":
            print("You close the Ledger for now.\n")
            break

        page += 1

def read_entries():
    print("\nReading the Ledger...\n")

    folder_path = load_folder_path()
    if not folder_path:
        print("No folder path found. Please record a ritual first.")
        return

    ledger_file_path = os.path.join(folder_path, "ledger.txt")

    if not os.path.exists(ledger_file_path):
        print(f"No ledger found at '{ledger_file_path}'. Begin by recording your first ritual.")
        return

    try:
        with open(ledger_file_path, "r", encoding="utf-8") as ledger:
            raw_content = ledger.read()
            entries = [e.strip() for e in raw_content.split('---') if e.strip()]

            if not entries:
                print("The ledger is empty. The Watcher waits.")
                return

            search = input("Whisper a keyword to filter by (leave blank to skip): ").lower()
            date_filter = input("Speak a date (YYYY-MM-DD or just YYYY-MM) to filter by (leave blank to skip): ").strip()
            tag_filter = input("Search by tag (comma-separated, leave blank to skip): ").strip().lower()

            matched = []
            for entry in entries:
                if search and search not in entry.lower():
                    continue
                if date_filter and date_filter not in entry:
                    continue
                if tag_filter:
                    if "|" in entry:
                        tags_section = entry.split("|")[1].strip().lower()
                        if not any(tag.strip() in tags_section for tag in tag_filter.split(',')):
                            continue
                    else:
                        continue
                matched.append(entry)

            if not matched:
                print("No echoes align with your words, time, or tags.")
                return

            sort_order = input("Read the ledger in what order? (newest/oldest): ").strip().lower()
            
            def extract_timestamp(entry):
                # This assumes that the timestamp is always in the format: [YYYY-MM-DD HH:MM:SS]
                start = entry.find("[") + 1
                end = entry.find("]")
                timestamp_str = entry[start:end]
                return datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                
            # Sort entries based on user preference (newest/oldest)
            reverse_sort = sort_order != "oldest"  # newest first if sort_order is "newest"
            matched.sort(key=extract_timestamp, reverse=reverse_sort)

            paginate_entries(matched)

    except FileNotFoundError:
        print(f"No ledger found at '{ledger_file_path}'. Begin by recording your first ritual.")

def main():
    create_db()
    while True:
        print("\nChoose your path:")
        print("1. Record a new ritual")
        print("2. Read the Ledger")
        print("3. Exit the sanctum")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            record_ritual()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            print("Farewell, Initiate.\n")
            break
        else:
            print("That path is unknown to the daemon. Choose again.")

if __name__ == "__main__":
    main()

