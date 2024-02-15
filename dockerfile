FROM python:alpine3.17
WORKDIR /app 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 
COPY . /app /backend 
ENTRYPOINT ["python","app.py"]

