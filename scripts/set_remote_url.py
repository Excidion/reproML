import subprocess
import sys

check_inside_git_repo = "git rev-parse --is-inside-work-tree".split()
if not subprocess.run(check_inside_git_repo, capture_output=True).returncode:
    subprocess.run(["git", "remote", "set-url", "origin", sys.argv[1]], check=True)
