# command to wrap:
# git log --since="2026-04-01" --until="2026-04-18" --pretty=format:"%H|%ad|%an|%s" --date=short

import subprocess

def get_raw_log(repo_path: str, since: str, until: str) -> str:
    result = subprocess.run(
        ["git", "log",
            f"--since={since}",
            f"--until={until}",
            "--pretty=format:%H|%ad|%an|%s",
            "--date=short"], 
            text=True,
            capture_output=True,
            cwd=repo_path
    )
    if result.returncode !=0:
        raise RuntimeError(result.stderr)
    return result.stdout