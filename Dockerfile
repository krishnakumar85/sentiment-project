# Step 1: Start with a base image (Python)
FROM python:3.9-slim

# Step 2: Set environment variables
ENV PYTHONUNBUFFERED=1

# Step 3: Set the working directory inside the container
WORKDIR /app

# Step 4: Copy the requirements file into the container
COPY requirements.txt /app/

# Step 5: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 6: Copy the rest of your application code
COPY ./pythonProjectFlask/ /app/

# Step 7: Expose the port your Flask app will run on
EXPOSE 5000

# Step 8: Define the command to run your app
CMD ["python", "app.py"]
