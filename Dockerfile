# Use the official Python base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files to the working directory
COPY . /app

# Expose port (change if needed)
EXPOSE 8000

# Set the startup command
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
