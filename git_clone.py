import git
import os
import logging

# setting logging level to debug
logging.basicConfig(level=logging.DEBUG)

# assign user, password, and repo as variables
user = "pat"
password = "ho4tla6r4osly74n6dxg32k4hm2x6kjx6pif4al5vjkp44gil2pq"
repo = "logi-api"

# create the repository url using the variables
repo_url = f"https://{user}:{password}@dev.azure.com/AHITL/SW%20Infrastructure/_git/{repo}"

# set local path to a directory named workspace
local_path = "./workspace/logi-api"

# create the workspace directory if it doesn't exist
if not os.path.exists("./workspace"):
    os.mkdir("./workspace")

# if the local path does not exist, clone the repository
# otherwise, skip the clone and log a message
if not os.path.exists(local_path):
    git.Repo.clone_from(repo_url, local_path)
else:
    logging.info(f"{local_path} already exists, skipping clone.")
