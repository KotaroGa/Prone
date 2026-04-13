# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app
 
ENV PYTHONUNBUFFERED=1

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the app
CMD ["python", "src/main.py"]
