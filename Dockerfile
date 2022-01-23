FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV FLASK_APP ./ytpl_sorted/webapi.py
CMD [ "python", "ytpl_sorted/webapi.py"]
