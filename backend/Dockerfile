FROM python:3.11-alpine 

WORKDIR /app/backend

#Replaces pip
RUN pip install uv 
COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --system

# Source build dir to inside the container
COPY . .

# Hint that container will be listening for traffic on this port
EXPOSE 8080

# Remove --reload when finished with dev
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
