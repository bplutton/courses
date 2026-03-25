# Exercise: Log Analyzer

## Overview

You're the sysadmin for a web server that's been acting up. Your boss hands you a log file and says: *"Tell me what happened."* Your job is to build a bash script that answers key questions about the log — using only the command-line tools you've learned.

This is a **guided walkthrough**. Follow each step, write the command, and run your script to see the results. By the end, you'll have a working log analysis tool.

## What You'll Practice

- `grep` — search for patterns in text
- `wc` — count lines, words, characters
- `sort` and `uniq` — find and count unique values
- `cut` and `awk` — extract specific fields
- Pipes (`|`) — chain commands together
- Output redirection (`>`, `>>`) — save results to files

## Setup

> **Already forked from a previous assignment?** Pull the latest updates:
> ```bash
> git remote add upstream https://github.com/blkfin/courses.git   # only needed once
> git fetch upstream
> git merge upstream/main
> ```

Navigate to the exercise directory:
```bash
cd it612/exercises/log-analyzer/
```

You should see two files:
- `server.log` — the log file you'll analyze
- `analyze.sh` — the starter script where you'll write your commands

Take a quick look at the log file to get oriented:
```bash
head -10 server.log
```

Each line follows a format: `DATE TIME LEVEL MESSAGE`. The levels are `INFO`, `WARN`, and `ERROR`.

---

## Step 1: Count the Basics

Open `analyze.sh` in the editor. Find **Step 1** and write commands that:

1. **Count total lines** in the log file using `wc -l`
2. **Count ERROR lines** using `grep` and `wc -l` together (piped)
3. **Count WARN lines** the same way

After each command, use `echo` to label the output so it's readable.

**Run your script** to check:
```bash
bash analyze.sh
```

You should see something like:
```
=== Log Analysis Report ===

--- Line Counts ---
Total lines: 62
Error lines: 12
Warning lines: 6
```

> **Hint:** `grep "ERROR" server.log | wc -l` counts how many lines contain "ERROR".

---

## Step 2: Extract Unique Errors

Still in `analyze.sh`, find **Step 2**. The goal is to see *what kinds* of errors happened — not every individual line, just the distinct error messages.

1. Use `grep` to find all ERROR lines
2. Pipe to `cut` or `awk` to extract just the message part (everything after the log level)
3. Pipe to `sort` and then `uniq` to remove duplicates

> **Hint:** `awk '{for(i=4;i<=NF;i++) printf "%s ", $i; print ""}'` grabs everything from the 4th field onward — that's the message after `DATE TIME LEVEL`.

**Run your script.** You should see a list of distinct error messages — no repeats.

---

## Step 3: Most Requested Endpoints

Find **Step 3**. Your boss wants to know which pages and API endpoints get the most traffic.

1. Use `grep` to find lines containing `GET` or `POST`
2. Use `awk` to extract just the HTTP method and path (fields 5 and 6)
3. Pipe through `sort | uniq -c | sort -rn` to count and rank them

> **What does each piece do?**
> - `sort` groups identical lines together (required before `uniq`)
> - `uniq -c` collapses duplicates and adds a count
> - `sort -rn` sorts by count, highest first (`-r` = reverse, `-n` = numeric)

**Run your script.** You should see the busiest endpoints ranked by hit count.

---

## Step 4: Who Logged In?

Find **Step 4**. Let's figure out which users logged in and how many times.

1. Use `grep` to find lines that mention `session created for user=`
2. Use `grep -o` or `awk` to extract just the username
3. Pipe through `sort | uniq -c | sort -rn`

> **Hint:** `grep -o 'user=[a-z]*'` extracts just the `user=name` part from each matching line. The `-o` flag means "only print the matching part."

**Run your script.** You should see each user and their login count.

---

## Step 5: Save the Report

Find **Step 5**. Instead of printing to the screen, save the full report to a file called `report.txt`.

The simplest way: redirect the *entire script's output* when you run it:
```bash
bash analyze.sh > report.txt
```

But for this exercise, add a line at the end of your script that copies the output:
1. Add a final `echo` line: `echo "Report generated: $(date)"`
2. We'll run: `bash analyze.sh | tee report.txt` — this prints to screen AND saves to file

> **`tee` explained:** It reads from stdin and writes to *both* stdout (your screen) and a file. Named after a T-shaped pipe fitting that splits flow in two directions.

---

## Wrap-Up

When you're done, your script should produce a clean report covering:
- Line counts (total, errors, warnings)
- Unique error messages
- Top endpoints by traffic
- User login activity

**Submit:**
```bash
bash analyze.sh | tee report.txt
git add -A
git commit -m "Exercise: Log Analyzer"
git push
```

Submit the URL to your GitHub repository.

---

## Bonus (Optional)

If you finish early, try adding:
- **Time range:** How many minutes does the log cover? (Hint: compare the first and last timestamps)
- **Error rate:** What percentage of log lines are errors? (Hint: bash can do arithmetic with `$(( ))`)
- **Response times:** What's the slowest API response? (Hint: `grep -o '[0-9]*ms'` + `sort -n`)
