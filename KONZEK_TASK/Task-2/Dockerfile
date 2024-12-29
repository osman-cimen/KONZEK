# Use the official Python image as the base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY python_http_server.py .

# Expose the application port
EXPOSE 8080

# Define the command to run the application
CMD ["python", "python_http_server.py"]
