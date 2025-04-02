FROM python:3.11-slim

COPY requirements.txt .

RUN apt update && apt install -y git && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .

CMD ["python","app.py"]

#ENTRYPOINT ["flask"]
#CMD ["run"]
#EXPOSE 5000