FROM python:3.8-slim
RUN mkdir /djangocharts
WORKDIR /djangocharts
COPY . .

RUN pip install -r requirements.txt \
 && rm -rf requirements.txt

EXPOSE 8000
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000" ]
