# Que:-  Install Docker and create Dockerfiles to containerize applications?

**To install Docker and containerize an application using a Dockerfile, follow these two main processes:**

 - first, the installation and verification of Docker, and
  second, the steps for creating the Dockerfile, building an image, and running a container. 

## Part 1: Install and Verify Docker 
- The specific installation steps depend on your operating system. Docker Desktop is recommended for Windows and macOS, while Linux users can install the Docker Engine. 

**Download Docker:** Visit the official Docker website and download the appropriate installer for your OS (Windows, macOS, or Linux).

**Run the Installer:**

- Windows/macOS: Double-click the downloaded installer file and follow the on-screen instructions. For Windows, ensure the option to use WSL 2 (Windows Subsystem for Linux 2) is selected during installation if available, as it offers better performance.

- Linux: Follow the instructions for setting up the official Docker apt repository and install the necessary packages using your system's package manager (e.g., apt, yum).

**Verify the Installation:**
 Open your terminal or command prompt and run the following command to check the installed Docker version:

```bash
docker --version
```

- You can also run a test container to ensure everything is working correctly:

```bash
docker run hello-world
```

- This command downloads and runs a test image, printing a confirmation message if successful.
---

## Part 2: Create Dockerfiles to Containerize Applications 
Containerizing an application involves creating a text file named Dockerfile with no file extension that contains instructions for building a Docker image. 

1. **Create a Project Directory**

- Set up a new folder for your application and navigate into it: 
```bash
mkdir my-docker-app
cd my-docker-app
```
Inside this directory, place your application code and any dependency files (e.g., requirements.txt for Python, package.json for Node.js). We are going to create ```requirements.txt```

2. **Write the Dockerfile**

- Create a file named ```Dockerfile``` (with no file extension) in your project directory and add the necessary instructions. Each instruction creates a new layer in the Docker image. 

**for our Python application:**
```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9 

# Set the working directory in the container
WORKDIR /app 

# Copy the dependency file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt 

# Copy the current directory contents into the container at /app
COPY . . 

# Run the application when the container starts
CMD ["python", "run.py"]
``` 
3. **Build the Docker Image**

- Open your terminal, navigate to your project directory, and run the docker build command. The -t flag tags your image with a human-readable name, and the . at the end specifies the current directory as the build context: 

```bash
docker build -t my-app-image .
```
4. **Run the Containerized Application**

- Once the image is built, you can run it as a container using the docker run command. The -p flag maps a port on your host machine to a port in the container, and -d runs the container in detached mode (in the background): 

```bash
docker run -d -p 5000:5000 my-app-image
```
Your application should now be running in a Docker container and accessible via http://localhost:5000 in your web browser. You can view running containers with docker ps.