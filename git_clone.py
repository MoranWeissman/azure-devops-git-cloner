import git
import os
import logging

# Get the values of the environment variables, or use the default values
user = os.environ.get("user", "pat")
organization = os.environ.get("organization", "AHITL")
password = os.environ.get("password")
repository = os.environ.get("repository")
branch = os.environ.get("branch")
project = os.environ.get("project")

# Replace the leading 'refs/heads/' from the 'branch' value
branch = branch.replace('refs/heads/', '')

# Check if the required environment variables are set
if not all(var in os.environ for var in ['password', 'repository', 'branch', 'project']):
    raise ValueError("Missing required environment variables")

# Check for spaces in the project variable
if " " in project:
    # Replace spaces with "%20"
    project = project.replace(" ", "%20")
    logging.debug(f"Project variable updated: {project}")

# Set local path variable
local_path = f"/workspace/{repository}"

# Configure logging settings
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Create the repository URL using the variables
repo_url = f"https://{user}:{password}@dev.azure.com/{organization}/{project}/_git/{repository}"
logging.debug(f"Repository URL: {repo_url}")

# create the workspace directory if it doesn't exist
if not os.path.exists("/workspace"):
    os.mkdir("/workspace")
    logging.debug("Workspace directory created")

# if the local path does not exist, clone the repository
# otherwise, skip the clone and log a message
if not os.path.exists(local_path):
    git.Repo.clone_from(repo_url, local_path, branch=branch)
    logging.debug(f"Repository cloned to {local_path}")
else:
    logging.info(f"{local_path} already exists, skipping clone.")
