FROM python:3.7-slim

WORKDIR /usr/src/payout

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./payout.py" ]