FROM tensorflow/tensorflow
MAINTAINER lewuathe

USER root

RUN mkdir -p /srv/tf-cluster
RUN mkdir /srv/tf-cluster/config

ADD job.py /srv/tf-cluster

EXPOSE 2222

WORKDIR /srv/tf-cluster
ENTRYPOINT ["python", "job.py"]
