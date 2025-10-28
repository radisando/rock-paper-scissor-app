FROM python:3.12.9

WORKDIR /app

# copy requirements and install
COPY requirements.docker.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade pip
RUN pip install -e .
RUN pip install --no-cache-dir -r requirements.txt

# Copy RPS Package, code and model folder
COPY api /app/api
COPY rps_package /app/rps_package
COPY models /app/models

# expose port and run uvicorn
ENV PORT=8000
EXPOSE 8000
CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
#CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
