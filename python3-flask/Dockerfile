FROM ubuntu:xenial
MAINTAINER CUI Wei <ghostplant@qq.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y
RUN apt-get install -y --no-install-recommends python3-flask && \
	rm -rf /var/lib/apt/lists/* /var/cache/apt/*.bin /var/cache/apt/archives/*.deb
ADD app.py /usr/local/bin
CMD ["/usr/local/bin/app.py"]
EXPOSE 8080

