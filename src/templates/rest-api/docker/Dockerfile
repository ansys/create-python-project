FROM python:3.10-alpine

RUN apk update
RUN pip install --upgrade pip

WORKDIR /app
COPY . /app
RUN pip --no-cache-dir install -r requirements.txt

CMD ["python3", "./src/app.py"]