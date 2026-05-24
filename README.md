# Log Parser

A beginner-friendly Python log parser that filters critical events from large log files.

## Why I built this

SOC analysts deal with thousands of log lines every day. 
Reading them manually is impossible. This script scans all 
log entries and pulls out only the HIGH and CRITICAL ones — 
so you focus on what matters first.

## What it does

- Reads a log file line by line
- Detects severity levels: INFO, WARNING, HIGH, CRITICAL
- Counts how many of each severity exists
- Saves HIGH and CRITICAL lines to alerts.txt
- Prints a summary report

## Usage

```bash
python log_parser.py sample.log
```

Or just run with the default sample file:
```bash
python log_parser.py
```

## Sample output
