# docker: brief report

### 1. what is docker, and why is it useful in data science?

docker is a platform that packages applications and their dependencies into containers. it helps data scientists create consistent environments, avoid dependency conflicts, and run projects reliably across different machines.

### 2. difference between an image and a container

- **image:** a read-only template containing the application and everything needed to run it.
- **container:** a running instance of an image.

### 3. purpose of dockerfile instructions

- **from:** specifies the base image.
- **workdir:** sets the working directory inside the container.
- **copy:** copies files from the host machine into the image.
- **run:** executes commands during image creation.
- **cmd:** specifies the default command executed when the container starts.
