FROM python:3.11-alpine 

WORKDIR /app/backend

# Get REQ
COPY requirements.txt .
RUN pip install -r requirements.txt

# Source build dir to inside the container
COPY . .

# Hint that container will be listening for traffic on this port
EXPOSE 8080

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
