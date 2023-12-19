FROM python:3.11.7-slim
LABEL authors="shara"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["faststream", "run", "subscriber:app"]