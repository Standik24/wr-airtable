FROM quay.io/keboola/docker-custom-python:latest

WORKDIR /app


RUN pip install pytest==7.2.1 \
&& pip install https://github.com/keboola/python-docker-application/zipball/master \
&& pip install sshtunnel==0.4.0

COPY . /app/src


# run main.py in Python
CMD ["python", "-u", "main.py"]
