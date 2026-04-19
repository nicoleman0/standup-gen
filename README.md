# standup-gen

Generates a standup summary from a git repository's commit history. Optionally uses AI (via Groq) to turn the raw commits into a short, readable paragraph you can copy and send.

## Setup

1. Clone the repo and install dependencies:

```bash
pip install -e .
```

2. Create a `.env` file with your Groq API key (only needed for `--summarize`):

```
GROQ_API_KEY=your_key_here
```

## Usage

```bash
standup /path/to/your/repo --since 1.day.ago --summarize
```

**Arguments:**

| Flag | Default | Description |
|------|---------|-------------|
| `repo_path` | *(required)* | Path to the git repository |
| `--since` | `7.days.ago` | How far back to look |
| `--until` | `now` | End of the range |
| `--author` | *(none)* | Filter to a specific author |
| `--summarize` | off | Use AI to write a prose summary |
| `--output` | *(stdout)* | Write output to a file instead |

## Personalizing the AI summary

The AI prompt in `standup/summarizer.py` is written for a developer named Nick. If you're sharing this with others, update the system prompt to use the right name:

```python
"content": (
    "You are helping <YOUR NAME> write their daily standup update. "
    "<YOUR NAME> is the developer who wrote all the commits. "
    ...
),
```

You may also want to adjust the tone or format instructions in that same string.
