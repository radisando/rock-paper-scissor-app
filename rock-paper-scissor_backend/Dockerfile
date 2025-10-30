# rock-paper-scissor_backend/Dockerfile
FROM python:3.10-slim-bullseye
#FROM python:3.12.9

# Avoid prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PORT=8000

WORKDIR /app

# copy requirements and install
COPY requirements.docker.txt /app/requirements.txt

# system deps needed for some python packages (pillow, opencv)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# Install pip deps
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r /app/requirements.txt
#RUN pip install --no-cache-dir --upgrade pip
#RUN pip install -e .
#RUN pip install --no-cache-dir -r requirements.txt


# Copy RPS Package, code and model folder
COPY api /app/api
COPY rock_paper_scissor /app/rock_paper_scissor
COPY models /app/models

# Create a logs dir that the app will be able to write to
RUN mkdir -p /app/logs && chmod -R 0777 /app/logs

# expose port and run uvicorn
ENV PORT=8000
EXPOSE 8000
#CMD uvicorn api.main:app --host 0.0.0.0 --port $PORT
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
