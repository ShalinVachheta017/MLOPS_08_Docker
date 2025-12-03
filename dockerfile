# Use the official Python 3.11 slim image as the base image
# Slim images are smaller and more efficient for production
FROM python:3.11-slim

# Set the working directory inside the container
# All subsequent commands will be executed from this directory
WORKDIR /app

# Copy the requirements file to the container
# This is done separately to leverage Docker's layer caching
# If requirements don't change, this layer can be reused
COPY . /app

# Install Python dependencies from requirements.txt
# --no-cache-dir reduces the image size by not storing pip cache
RUN pip install --no-cache-dir -r requirements.txt


# Expose port 5000 to allow external access to the Flask application
# This is the port that the Flask app runs on
EXPOSE 5000

#Define environment variable for Flask
ENV FLASK_APP=app.py

# Define the command to run the application
# This starts the Flask application when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]