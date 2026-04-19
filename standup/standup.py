import argparse
from standup.git import get_raw_log, parse_log
from standup.formatter import format_log

parser = argparse.ArgumentParser(description="Generate a standup summary from git log.")
parser.add_argument("repo_path", help="Path to the git repository")
parser.add_argument("--since", default="7.days.ago", help="Start date for git log (default: 7.days.ago)")
parser.add_argument("--until", default="now", help="End date for git log (default: now)")

args = parser.parse_args()
raw_log = get_raw_log(args.repo_path, args.since, args.until)
commits = parse_log(raw_log)
summary = format_log(commits)
print(summary)