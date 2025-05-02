# Ritual Journal

> **A minimal terminal-based ritual and mood tracker.**  
> **Ritual Journal** is a tool for those who understand that discipline is a form of magic.  
> Track your rites. Record your moods. Witness your becoming.

---

## About

Built in Python and powered by SQLite, Ritual Journal is a minimal, local-first system for tracking thoughts, habits, and symbolic actions — daily rites performed in the service of growth, clarity, and mastery.

> It is not a planner.  
> It is not a productivity hack.  
> It is a ledger of devotion.

Entries are recorded not as tasks, but as rituals: moments of intention, reflection, and momentum toward a greater work — yourself.

> **The Watcher sees. The Ledger remembers. You become.**

Built for **DaemonOS**. Offered to the few.  
The Ritual Journal was made for daemons.

---

## First Ritual - A Demo  
_Screenshots of Ritual Journal v.1 running in Arch Linux._

### Part I. — Record a Ritual

Click `[1]` to record your ritual. We will explore the functionality of `[2]` and `[3]` later.

https://private-user-images.githubusercontent.com/208912497/439768862-d7e6d2f9-e4e2-45c2-aa99-f5627cc11362.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDYxNTAwNzksIm5iZiI6MTc0NjE0OTc3OSwicGF0aCI6Ii8yMDg5MTI0OTcvNDM5NzY4ODYyLWQ3ZTZkMmY5LWU0ZTItNDVjMi1hYTk5LWY1NjI3Y2MxMTM2Mi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTAyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUwMlQwMTM2MTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1hNmU4NmJkOWJmMTYyZGUzMDRlZDg2NTQxNThlYjljNzY0NjkzOTQzNDg0NmVhYWNiNmI2ZWY4NDQyM2M4YjY5JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Vo3l381XjE3fA-gkob68z-X1O1_T9ELxe7pTRk2Fluo

This opens up dialogue:

https://private-user-images.githubusercontent.com/208912497/439769024-121a9bf9-6c1b-46a1-8b35-319599af2929.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDYxNTAwNzksIm5iZiI6MTc0NjE0OTc3OSwicGF0aCI6Ii8yMDg5MTI0OTcvNDM5NzY5MDI0LTEyMWE5YmY5LTZjMWItNDZhMS04YjM1LTMxOTU5OWFmMjkyOS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTAyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUwMlQwMTM2MTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02YTAzYWJjZWVjNzY3ZGE2ZjcwNTYwOTA2ZGJmNzI4ZTcyODdiMzJmZDhjZWUyMzIxY2I2NjE0YzhjYmQ0Mjc1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.IOKQHX5gOnicYBnClvpmcPLTKK1f5N-OsomvWc0Db7w

#### Input Fields:

1. **Name your completed ritual** – A title or short description.  
2. **Leave an offering of detail (optional)** – Full description of the ritual.  
3. **Mark the category (optional)** – A single keyword for grouping.  
4. **Inscribe your tags (comma-separated, optional)** – For flexible filtering.  
5. **Offer a mood sigil (emoji or symbol, optional)** – A mood glyph or emotional marker.

https://private-user-images.githubusercontent.com/208912497/439769063-1ad66575-6d9f-4800-9962-6b385b6e794a.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDYxNTAwNzksIm5iZiI6MTc0NjE0OTc3OSwicGF0aCI6Ii8yMDg5MTI0OTcvNDM5NzY5MDYzLTFhZDY2NTc1LTZkOWYtNDgwMC05OTYyLTZiMzg1YjZlNzk0YS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTAyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUwMlQwMTM2MTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1iMmNlMzA3ZmUyZDY5YTNiYTgxMzhjYjUxOTNmN2FlODdiYTQ2Njg3ZmQ3OThlMzZlMzBlOWFkMzFmNjkzNjc4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.xyS6CfVCsGBarVXZNyNgEhKRNH2Enqunsgmq3sbpKXM

To complete the note, type `/END` or `/end`. Case-insensitive.

The script will then prompt you to optionally watch the daemon “etch” the ritual:

https://private-user-images.githubusercontent.com/208912497/439769092-8d08b61f-8756-45b0-b999-678a54c6a368.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDYxNTAwNzksIm5iZiI6MTc0NjE0OTc3OSwicGF0aCI6Ii8yMDg5MTI0OTcvNDM5NzY5MDkyLThkMDhiNjFmLTg3NTYtNDViMC1iOTk5LTY3OGE1NGM2YTM2OC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTAyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUwMlQwMTM2MTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yMzJlZjJiM2QzNWVhZDQ3YWMyZWUwZmNjMWRkMDA0ZTg1MzI0ZTg5MjliMzc0YTFhZmY1YzM0YTVhNjdlNWJhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.pyWdcEC3IqQiihG1fdWDOccnNICv18ywCIiFZ6kZUKM

You will then be prompted to save your `ledger.txt` file to a folder:

https://private-user-images.githubusercontent.com/208912497/439769094-0880518f-510d-4ed8-b0c9-ac3bec2608b3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDYxNTAwNzksIm5iZiI6MTc0NjE0OTc3OSwicGF0aCI6Ii8yMDg5MTI0OTcvNDM5NzY5MDk0LTA4ODA1MThmLTUxMGQtNGVkOC1iMGM5LWFjM2JlYzI2MDhiMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTAyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUwMlQwMTM2MTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03YjU4YTg2MWYwZDkxYzc0NDYxMGJmZGFhNWY3ZDMyNmQyODI3ZWQ2Mzc1MmQxNzg0YzQ3OTYzYTAwZDhiNmU3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.szz85Z4ZxoQzvjXplzqGYaPdy8hfTxDe3V5yppYbRVE

**Note:** If you do not select a folder, it defaults to the current directory.

---

### Part II. — Read the Ledger

Click `[2]` to open and browse the ledger.

https://private-user-images.githubusercontent.com/208912497/439769093-9f398d01-f3c7-40e6-9927-3b761960ec63.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDYxNTAwNzksIm5iZiI6MTc0NjE0OTc3OSwicGF0aCI6Ii8yMDg5MTI0OTcvNDM5NzY5MDkzLTlmMzk4ZDAxLWYzYzctNDBlNi05OTI3LTNiNzYxOTYwZWM2My5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTAyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUwMlQwMTM2MTlaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02NGE3MDI2Mjc3M2E1MTk3NTRlNDdjZDYyNTZjMTE3NjAxNDRiOTYxMWE0Y2M1ODQwNTkxZGM4NTQxNDQzMTJjJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Gq2DKnPEBKzixjmAusolrkmgLaEQkx25VFv-mXznWGo

Sorting/filtering options:

1. **Keyword filter** – Matches any term in entries.  
2. **Date filter (YYYY-MM-DD or YYYY-MM)**  
3. **Tag filter (comma-separated)**  
4. **Order by (newest/oldest)**

https://private-user-images.githubusercontent.com/208912497/439769127-0c7d317f-e224-48bd-9477-15c2f85cbd00.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDYxNTAzNDIsIm5iZiI6MTc0NjE1MDA0MiwicGF0aCI6Ii8yMDg5MTI0OTcvNDM5NzY5MTI3LTBjN2QzMTdmLWUyMjQtNDhiZC05NDc3LTE1YzJmODVjYmQwMC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTAyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUwMlQwMTQwNDJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01YmUzYWRmNWVhZGI2YjRlMzU1MTNhNDE1YjYxNTFiN2QwNTU1ZTliZGY5ZTA3YzRjMjZkNWU2ZmQzM2I2OTI2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.e1C7yvAd7c1YRct_rD9Jy4QCr1T5v0GrW2hLS3Fu5RA

---

---

## Practices & Enhancements

Since this application runs on Linux machines, you can create a launchable desktop application and hotkey.

### Step 1. Make Ritual Journal Executable

```bash
cd /path/to/ritual-journal
chmod +x ritual-journal.py

## Step 2. Create Desktop Application
Create a .desktop file for desktop integration

```bash
nano ~/.local/share/applications/ritual-journal.desktop
```

Then add the following to the file, adjusting the paths as needed

```ini
[Desktop Entry]
Version=1.0
Name=Ritual Journal
Comment=A ritual journaling and mood tracker. Made for daemons.
Exec=/path/to/ritual-journal/.venv/bin/python /path/to/ritual-journal/ritual-journal.py
Icon=/path/to/ritual-journal/icon.png
Terminal=true
Type=Application
Categories=Utility; Application;
```

>- `Exec`: Points to the Python interpreter in your virtual environment and runs the `ritual-journal.py` script.

>- `Icon`: You can specify the path to an icon file for the application (PNG, SVG, etc.). If you don't have an icon, you can leave this out or use a generic one.

>- `Terminal=true`: Ensures the terminal opens when launching the app, so you can view any logs or output.

>- `Categories`: This will categorize the app in the application menu (feel free to adjust if you'd like to categorize it differently).

*Save and close the file (`Ctrl+X`, `Y`, then `Enter`).*

And finally, we can now, make the `.desktop` file executable:

```bash
chmod +x ~/.local/share/applications/ritual-journal.desktop
```


# Step 3. Launch Ritual Journal
Using the .desktop file: You can now search for "Ritual Journal" in your application menu (e.g., GNOME or KDE) and launch it directly from there.

https://private-user-images.githubusercontent.com/208912497/439769128-dc1666d8-39e9-4c92-bb95-c60a4fad4d8c.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NDYxNTAzNDIsIm5iZiI6MTc0NjE1MDA0MiwicGF0aCI6Ii8yMDg5MTI0OTcvNDM5NzY5MTI4LWRjMTY2NmQ4LTM5ZTktNGM5Mi1iYjk1LWM2MGE0ZmFkNGQ4Yy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNTAyJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDUwMlQwMTQwNDJaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xMjA2Y2VlMzYzNjA4NGI2YTRmOGZiMTU2ZGZmYzgwZDRhMGRhODk0NTRkMGI5OWY0ZDBiMTFlY2E3MTkyMTcwJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.-ESTzxNUtObtlBvR0yX_xc18UwwTG1KQW3ERFu5uqvg

## Step 4. Setup a Hotkey to Launch Ritual Journal in GNOME (Optional)
*I like GNOME, okay.*

1. Open GNOME Settings application: 
	- Press <code>Super</code> (Windows key) and search for "Settings"
2. In the left sidebar, select <strong>Keyboard</strong>
3. Scroll down and click <strong>Custom Shortcusts</strong>
4. Click the + button to add a new custom shortcut
5. In the <strong>Name</strong> field, give your shortcut a name, like "Launch Ritual Journal."
6. In the <strong>Command</strong> field, enter the full path to your <code>.desktop</code> file. For example:

```bash
/usr/share/applications/ritual-journal.desktop
```

7. Click <strong>Set Shortcut</strong>, then press the key combination you want to assign to the hotkey (e.g., <code>Ctrl+Alt+R)</code>.
8. Press <strong>Add</strong> to save the new shortcut.

Now, pressing your chosen hotkey will launch <strong>Ritual Journal.</strong>

## Example for Ritual Journal

In the case of **Ritual Journal**, we want to:

1. Activate the virtual environment (`.venv`).
2. Run the `ritual-journal.py` script.

We can combine these two commands using `bash -c` to ensure that the virtual environment is activated before running the Python script.

```ini
Exec=bash -c "source /path/to/ritual-journal/.venv/bin/activate && python /path/to/ritual-journal/ritual-journal.py"
```

This tells the system to invoke a new Bash shell to accomplish a few things very conveniently: 

1. - `bash -c`: This tells the system to invoke a new Bash shell and execute the following commands.

2. `source /path/to/ritual-journal/.venv/bin/activate`: This activates the virtual environment. By using `source`, we're ensuring that the environment variables are set in the current shell session.

3. `&&`: This ensures that the next command (`python /path/to/ritual-journal/ritual-journal.py`) only runs if the previous command (activating the virtual environment) was successful.

4. `python /path/to/ritual-journal/ritual-journal.py`: Finally, this runs the `ritual-journal.py` script using Python from the activated virtual environment.

# The Path Forward
*Whispers of the next version*
### I will be adding additional features in the near future:

1. User-select text colors (Customize text colors)
2. User-select entries per page (Defaults to 5)
3. User-select save folder (Update current save_folder_path or upon new entry creation -- allows user to create several journals in different folders)
4. User-select working directory (Choose which ledger.txt file to view or work in - see #3)
5. Additional Sort/Filter Options ( include sort and filter option - date ranges or option to view a ledger.txt located in another folder)
6. Export entries to Markdown or plain text
7. Entry editing or deletion
8. Add "ritual streaks" or calendar view
9. Encrypt ledger or password protection

---

DaemonOS // Forged in Silence // 2025

---
