FROM public.ecr.aws/docker/library/python:3.11.1-slim-bullseye

RUN mkdir -p /app
WORKDIR /app

COPY src/ /app/src/



# install python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r /app/requirements.txt && pip install httpie && rm -rf /app/requirements.txt

COPY src/entrypoint.sh /app
WORKDIR /app/src

EXPOSE 8080
ENTRYPOINT ["/app/src/entrypoint.sh"]

