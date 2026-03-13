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