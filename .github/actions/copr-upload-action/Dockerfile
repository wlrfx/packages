# Container image that runs your code
FROM fedora:latest

# Install dependencies
RUN dnf -y install copr-cli rpkg @rpm-development-tools

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up (`entrypoint.sh`)
ENTRYPOINT ["/entrypoint.sh"]
