FROM python:3.12

WORKDIR /mySite

COPY requirements.txt /mySite/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /mySite/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

