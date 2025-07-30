# Use official Python image
FROM python:3.10

# Set working directory in container
WORKDIR /app

# Copy files into container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port FastAPI runs on
EXPOSE 8000

# Run the API using uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
