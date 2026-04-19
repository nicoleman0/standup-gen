# command to wrap:
# git log --since="2026-04-01" --until="2026-04-18" --pretty=format:"%H|%ad|%an|%s" --date=short

import subprocess
from standup.models import Commit

def get_raw_log(repo_path: str, since: str, until: str) -> str:
    """
    args: repo_path, since, until

    Fetches the specified raw git logs.
    """
    result = subprocess.run(
        ["git", "log",
            f"--since={since}",
            f"--until={until}",
            "--pretty=format:%H|%ad|%an|%s",
            "--date=short"], 
            text=True, # necessary to get a usable output 
            capture_output=True,
            cwd=repo_path # Without this, git log runs in whatever directory you're in
    )
    if result.returncode !=0:
        raise RuntimeError(result.stderr)
    return result.stdout

def parse_log(raw_log: str) -> list[Commit]:
    lines = raw_log.splitlines()
    return [Commit(*line.split("|")) for line in lines]