FROM python:3.9-slim-buster

RUN pip install --upgrade pip;

RUN mkdir -p /service
WORKDIR /service

COPY . /service

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -
RUN  ln -s /root/.poetry/bin/poetry /usr/bin/poetry
RUN poetry config virtualenvs.create false
RUN poetry install

EXPOSE 5000

CMD ["python", "main.py"]