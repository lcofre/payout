FROM pypy:3-slim

WORKDIR /usr/src/payout

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "pypy3", "./payout.py" ]