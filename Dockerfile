# Base Image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files to container
COPY process_data.py .
COPY data /app/data

# Install dependencies
RUN pip install pandas

# Default command
CMD ["python", "process_data.py"]