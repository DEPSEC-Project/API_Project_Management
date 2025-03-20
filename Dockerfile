FROM python:3.11-slim

COPY requirements.txt .

RUN pip install -r requirements.txt
COPY . . 

ENTRYPOINT ["flask"]
CMD ["run"]
EXPOSE 5000