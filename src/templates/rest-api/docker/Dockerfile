FROM python:3.10-alpine

RUN apk update
#RUN apk add py-pip
#RUN apk add --no-cache python3-dev
RUN pip install --upgrade pip

WORKDIR /app
COPY . /app
RUN ls -la /app
RUN pip --no-cache-dir install -r requirements.txt

CMD ["python3", "./src/app.py"]