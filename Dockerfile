# Use the official Python image as the base image
FROM python:3.11.0

# Install the application dependencies
RUN pip install -r requirements.txt

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the working directory
COPY . .

# Define the entry point for the container
CMD ["python", "app/flightssearch_bot.py"]