FROM python:3.9-slim-buster

# set environment variables
ENV user=pat
ENV password=""
ENV repository=""
ENV branch=""
ENV organization=""
ENV project=""

# create workspace directory
RUN mkdir /workspace

# install git
RUN apt-get update && apt-get install -y git

# copy the code to the container
COPY . /app
WORKDIR /app

# Install the Git module
RUN pip install -r requirements.txt

# run the script
CMD ["python", "git_clone.py"]