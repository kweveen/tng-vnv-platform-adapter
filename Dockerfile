FROM ubuntu:latest
MAINTAINER Luis Hens "luis.hens@atos.net"
RUN apt-get update -y && apt-get install -y python3 python3-dev python3-pip curl python-pip libcurl4-gnutls-dev libgnutls28-dev git
COPY . /app
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
#ENTRYPOINT ["python"]
#CMD ["main.py"]

RUN pip install git+https://osm.etsi.org/gerrit/osm/osmclient

EXPOSE 5001
CMD ["python3", "/app/main.py"]
#CMD ["python3", "/app/main.py"]
