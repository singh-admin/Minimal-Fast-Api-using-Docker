FROM python:3.6

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["run.py"]