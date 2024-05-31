FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy the script into the container
COPY generate_report.py .

# Install required Python packages
RUN pip install requests

# Run the script
CMD ["python", "generate_report.py"]
