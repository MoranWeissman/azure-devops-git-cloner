import git
import os
import logging

# assign environment variables
os.environ["user"] = "pat"
os.environ["password"]
os.environ["repo"]
os.environ["branch"]

# set variables
local_path = f"./workspace/{os.environ['repo']}"

# setting logging level to debug
logging.basicConfig(level=logging.DEBUG)

# create the repository url using the variables
repo_url = f"https://{os.environ['user']}:{os.environ['password']}@dev.azure.com/AHITL/SW%20Infrastructure/_git/{os.environ['repo']}"

# create the workspace directory if it doesn't exist
if not os.path.exists("./workspace"):
    os.mkdir("./workspace")

# if the local path does not exist, clone the repository
# otherwise, skip the clone and log a message
if not os.path.exists(local_path):
    git.Repo.clone_from(repo_url, local_path, branch=f"{os.environ['branch']}")
else:
    logging.info(f"{local_path} already exists, skipping clone.")
