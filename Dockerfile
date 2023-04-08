FROM python:3.8-slim
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip  \
    && pip install pipenv
RUN apt-get update && apt-get install python3-dev default-libmysqlclient-dev gcc -y
COPY ./requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/
# run entrypoint.sh
RUN ["chmod", "+x", "/usr/src/app/entrypoint.sh"]
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
