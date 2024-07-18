FROM python:3.12.3
RUN apt-get update

WORKDIR /app

COPY requirements.txt requirements.txt

ENV PIP_DOWNLOAD_CACHE "C:/Windows/Temp"
RUN --mount=type=cache,target="$PIP_DOWNLOAD_CACHE" \
    pip install -r requirements.txt

COPY . .

CMD [ "python", "app.py"]