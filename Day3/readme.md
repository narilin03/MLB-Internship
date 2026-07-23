# Day 3: Updated Student Record Management System (Persistent Version)

## 📌 Project Overview
This project builds upon the original console-based application by adding persistent data storage. By integrating Python's native file-handling capabilities with the `json` module, the program can now save, modify, load, and retain data permanently across system sessions.

---

## 💡 What I Learned Today
* **File I/O Operations**: Mastered opening, reading (`r`), and writing (`w`) raw application text streams inside clean Python contexts using the `with` statement wrapper.
* **Serialization & Deserialization**: Discovered how to translate active runtime Python dictionaries into physical string structures (`json.dump`) and vice-versa (`json.load`).
* **Bulletproof Exception Handling**: Implemented multi-layered `try-except` guard loops protecting user inputs against random typecasting bugs (like text values typed inside GPA prompts) and unexpected disk access issues.

---

## 🔄 How File Handling and JSON Work Together
Python's core file configurations only accept plain textual character flows. This creates a functional gap when trying to write composite structural objects directly to a drive.

1. **Saving Data**: The `json.dump()` utility standardizes complex embedded dictionary values into unified JSON strings before executing the file object's write method.
2. **Loading Data**: On system initialization, the `json.load()` function takes over by reading the file's JSON string contents and remapping them back into real, operational Python dictionary elements.

This combination enables rapid structural database access while storing objects cleanly on disk.

---

## ⚡ Challenges Faced & Solutions
* **Handling Empty or Missing Files**: On the initial startup run, the program threw missing file errors if `students.json` didn't exist yet. 
  * *Solution*: Implemented the `os.path.exists()` check within the loading module to safely initialize an empty dictionary if no previous save exists.
* **Corrupted JSON Structures**: Manually altering raw source values in the database text occasionally caused total runtime crashes from broken string parsing logic.
  * *Solution*: Isolated structural operations inside target `try-except (json.JSONDecodeError)` containment blocks to reset gracefully without losing state.
