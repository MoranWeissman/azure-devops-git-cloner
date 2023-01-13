import os
import git
from git import transport

# Get the repo URL from the environment variable
repo_url = os.getenv("REPO_URL", "https://dev.azure.com/AHITL/SW%20Infrastructure/_git/logi-api")

# Get the PAT from the environment variable
pat = os.getenv("PAT", "apfm22yjz5gpcbgock3yqaisz6mx5acykllhdt7y56hpcu7wy4aa")

# Get the branch name from the environment variable
branch = os.getenv("BRANCH", "main")

# Get the current working directory
current_dir = os.getcwd() + "/workspace"

# Check if the directory already exists
if os.path.exists(current_dir):
    print("Directory already exists, deleting it")
    os.rmdir(current_dir)

# Create the directory
os.mkdir(current_dir)

try:
    git.Repo.clone_from(
        repo_url,
        current_dir,
        branch=branch,
        env={
            "GIT_ASKPASS": "echo",
            "GIT_TERMINAL_PROMPT": "0",
        },
        depth=1,
        progress=True,
        auth=transport.HTTPBasicAuth("pat", pat),
    )
    print("Repository cloned successfully")
except Exception as e:
    print(f"Error occured while cloning the repository {e}")
    exit(1)
