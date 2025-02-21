FROM python:3.12

WORKDIR /app

COPY ./app /app
COPY flag.txt /flag.txt
COPY requirements.txt .


EXPOSE 9000
RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:9000", "wsgi:app"]

