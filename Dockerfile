FROM python:3.8
USER root

COPY ./lambda_function.py /code/
COPY ./requirements.txt /code/
WORKDIR /code

RUN apt-get update \
&&  apt-get install -y zip\
&&  apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt -t ./
RUN pip install awscli
RUN zip -r lambda.zip .

CMD ["cp","lambda.zip","/zip/"]
