FROM python:3.9

RUN apt-get update && apt-get install -y pipenv

COPY ["Pipfile", "Pipfile.lock", "/usr/src/"]

WORKDIR /usr/src

RUN pipenv install

COPY [".", "."]

RUN pipenv run flask db upgrade

EXPOSE 5000

CMD ["pipenv", "run", "flask", "run"]
