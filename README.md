# azure-devops-git-cloner
A simple tool that clones a Git repository from Azure DevOps to the current working directory
<br>
<br>
# Git Clone Utility

This code provides a simple utility to clone a Git repository. It uses the GitPython library to perform the cloning. The required information, such as the repository URL, user, password, and other details, are passed as environment variables. The code sets default values for these variables if they are not set.

## Features

- Clones the repository to the specified local path, or skips the cloning if the local path already exists.
- Replaces spaces in the project variable with `%20`.
- Logs debug and error messages for easier debugging.

## Usage

1. Set the required environment variables. These include `user`, `password`, `repository`, `branch`, and `project`.
2. Run the code.
3. Check the logs for messages and debugging information.

## Environment Variables

| Variable Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| `user` | No | `pat` | The username to use when cloning the repository. |
| `organization` | No | `AHITL` | The organization name to use when cloning the repository. |
| `password` | Yes | N/A | The password to use when cloning the repository. |
| `repository` | Yes | N/A | The name of the repository to clone. |
| `branch` | Yes | N/A | The name of the branch to clone. |
| `project` | Yes | N/A | The name of the project to clone. |

## Requirements

- Python 3.x
- GitPython library

## License

This code is released under the MIT License.

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
