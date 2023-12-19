FROM tiangolo/uvicorn-gunicorn-fastapi
LABEL authors="shara"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]