FROM python:3.10-alpine

#RUN apt update && apt install make

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

COPY run_web.sh /run_web.sh

RUN chmod +x /run_web.sh