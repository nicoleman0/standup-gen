# Changelog/Standup Generator -- Project Plan

---

**Goal**

A CLI tool you run from your terminal, pointed at a git repo, that outputs a formatted summary of commits for a given date range.

---

**Core features (v1)**

- Specify a repo path, start date, and end date
- Run `git log` via `subprocess` and capture the output
- Parse each commit into structured data (hash, date, author, message)
- Print a clean formatted summary to stdout

---

**Suggested structure**

```
standup/
├── standup.py        # entry point, CLI definition
├── git.py            # git log invocation and raw output parsing
├── formatter.py      # takes parsed commits, returns formatted string
└── models.py         # Commit dataclass
```

---

**Build order**

1. Define a `Commit` dataclass in `models.py` with fields: `hash`, `date`, `author`, `message`
2. Write a function in `git.py` that runs `git log` with `--pretty=format` and a date range, returns raw output
3. Write a parser in `git.py` that turns that raw output into a list of `Commit` objects
4. Write a formatter in `formatter.py` that takes the list and returns a readable string
5. Wire it together in `standup.py` with a basic `argparse` CLI

---

**The `git log` command you'll be wrapping**

```bash
git log --since="2025-04-01" --until="2025-04-18" --pretty=format:"%H|%ad|%an|%s" --date=short
```

Each line comes back as pipe-delimited fields, which makes parsing straightforward.

---

**CLI interface (target)**

```bash
python standup.py --repo /path/to/repo --since 2025-04-01 --until 2025-04-18
```

---

**What to add once v1 works**

- `--author` filter to scope to your commits only
- `--output` flag to write to a `.md` file instead of stdout
- Anthropic API call to summarise the commit list into plain English (this becomes the "Alex update" generator)
