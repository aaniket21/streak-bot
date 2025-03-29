import os
from datetime import datetime

# Ensure we're in the right directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Update log file
with open("dummy_log.txt", "a") as f:
    f.write(f"Auto-commit at {datetime.now()}\n")

# Git operations
os.system("git add dummy_log.txt")
os.system(f'git commit -m "Auto-commit: {datetime.now()}"')
os.system("git pull --rebase")  # Avoid conflicts
os.system("git push origin main")