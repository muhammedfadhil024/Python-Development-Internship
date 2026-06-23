# Employee Payroll File Manager

A lightweight, console-driven automation and data persistence tool written in pure Python. This project serves (File Handling & Automation Tool).

## Overview
This application shifts from volatile, in-memory data storage to persistent flat-file tracking. It implements an interactive command-line interface (CLI) that allows real-time data input, updates an underlying plain-text database, dynamically computes aggregated workforce payroll analytics, and compiles structured file summaries.

## Implemented Core Concepts

The system architecture completely consolidates the Phase 2 milestone requirements specified in the internship handbook:
* **Interactive Control Flow Structure:** Employs an infinite evaluation loop (`while True`) paired with a multi-branch conditional system (`if-elif-else`) to route user operations smoothly.
* **Persistent File Input Streams (`read`):** Dynamically reviews local file architecture boundaries using the `os` framework, streaming raw records via `readlines()` inside safe context managers.
* **Persistent File Output Streams (`write`/`append`):** Employs conditional file modifiers (`"a"` for incremental record logging and `"w"` for fresh document compilations).
* **Text Deserialization & Formatting:** Strips residual invisible control layout characters (`.strip()`) and segments character groups (`.split(",")`) to map strings to numeric variables safely.

## System File Architecture

* `Employee Payroll File Manager.py`: The core application engine containing the execution flow, calculation logic, and menu terminal layout.
* `employees.txt`: The primary storage file acting as a flat-file database to persist employee records between script executions.
* `report.txt`: The auto-generated corporate overview document compiled by the system upon user request.

## Requirements
- Python 3.x

## How to Run the Application

1. Make sure Python 3.x is installed on your computer.
2. Place your script file in a folder.
3. Open your terminal or command prompt in that folder and run:
   ```bash
   python "Employee Payroll File Manager.py"
   ```
   ## Demo Video
   https://drive.google.com/file/d/1oT97e9VzzsEcZKJgj_T3jqgOrPuLHnK7/view?usp=share_link
