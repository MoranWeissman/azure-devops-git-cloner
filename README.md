# azure-devops-git-cloner
A simple tool that clones a Git repository from Azure DevOps to the current working directory
<br>
<br>
## Git Clone Script
This script is used to clone a git repository. It is designed to work with Azure DevOps and GitHub.
<br>
<br>
## Usage
Before running the code, make sure you have the following environment variables set:

* `password`: the password for the Azure DevOps account
* `repository`: the name of the repository you want to clone
* `branch`: the branch of the repository you want to clone
* `project`: the name of the project that the repository belongs to

You can also set the following optional environment variables:

* `user`: the username for the Azure DevOps account (default is "pat")
* `organization`: the name of the organization that the project belongs to (default is "AHITL")

The script will clone the repository to a directory called workspace in the current working directory. If the workspace directory does not exist, it will be created. If the repository has already been cloned to the specified local path, the script will skip the clone and log a message.
<br>
<br>
## How to run
The script is intended to be run with python.
```
python git_clone.py
```
<br>
<br>

## CI/CD pipeline
<br>

This pipeline is intended to be run on Azure DevOps, but it can be adapted to run on other platforms like GitHub Actions.

The pipeline has the following steps:

1. Bump patch version number: This step checks if the build was triggered by an individual commit, if so, it increments the patch version of the code in the VERSION file and makes a commit with the updated version.
2. Build and Push Docker Image: This step builds a Docker image from the Dockerfile and pushes it to GitHub Docker Registry.
3. Deploy: This step deploys the newly built image to the desired environment.

The pipeline is triggered when a new commit is made to the main branch.
<br>
<br>
## Docker Image
<br>
The script is intended to be run in a Docker container. A sample Dockerfile is provided in the repository to build the image.
<br>
<br>

```
FROM python:3.8-slim-buster

# set environment variables
ENV user=pat
ENV password=""
ENV repo=""
ENV branch=""

# create workspace directory
RUN mkdir /workspace

# install git
RUN apt-get update && apt-get install -y git

# copy the code to the container
COPY . /app
WORKDIR /app

# install the requirements
RUN pip install --upgrade pip && \
pip install -r requirements.txt

# run the script
CMD ["python", "git_clone.py"]
```
