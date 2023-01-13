# azure-devops-git-cloner
A simple tool that clones a Git repository from Azure DevOps to the current working directory using Go and go-git library.

## Getting Started

1. Make sure that you have Go installed and configured on your machine.
2. Make sure that you've installed the required dependencies using `go install gopkg.in/src-d/go-git.v4` command.
3. Create a new folder for your project and navigate to it in the command line.
4. Create a new file named `main.go` and copy the code into it.
5. Set the environment variables: `REPO_URL`, `PAT`, `BRANCH` with the appropriate values
6. Run the command `go build` to build the binary.
7. Run the command `./main` to execute the binary.

The tool will clone the repository to the directory where the binary is running.

## Environment Variables

The tool uses the following environment variables:
- `REPO_URL`: The URL of the repository in Azure DevOps.
- `PAT`: Personal Access Token that has permissions to clone the repository.
- `BRANCH`: The name of the branch that you want to clone.

Please make sure that these environment variables are set before running the binary.

## Dependencies

This tool depends on the following package:
- `gopkg.in/src-d/go-git.v4`: A high-level library for Git written in Go.

## Limitations

- This tool only supports Azure DevOps Git repositories.
- This tool only clones one branch of the repository at a time.

## Notes

- The tool assumes that the PAT you use has permissions to clone the repo, and that the repo url is correct.
- The tool clones the repository to the directory where the binary is running.
- The tool only support git protocol, it will not work with ssh protocol.

