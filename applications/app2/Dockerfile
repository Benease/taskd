# Use Alpine Linux as the base image
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the Python dependencies file
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 3001 to the outside world
EXPOSE 3001

# Command to run the Flask application
CMD ["python", "app.py"]

