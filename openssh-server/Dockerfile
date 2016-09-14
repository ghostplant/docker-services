FROM ubuntu:xenial
MAINTAINER CUI Wei <ghostplant@qq.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y
RUN apt-get install --no-install-recommends -y openssh-server uuid net-tools iproute2 psmisc vim-tiny inetutils-ping bash-completion whiptail rsync netcat-openbsd wget && \
	rm -rf /var/lib/apt/lists/* /var/cache/apt/*.bin /var/cache/apt/archives/*.deb
RUN echo "set backspace=indent,eol,start\nset nocompatible\n" >> /etc/vim/vimrc.tiny
RUN sed -i 's/#.*StrictHostKeyChecking ask/StrictHostKeyChecking no/g' /etc/ssh/ssh_config
RUN sed -i 's/^PermitRootLogin .*$/PermitRootLogin yes/g' /etc/ssh/sshd_config
RUN rm -f /etc/ssh/ssh_host_*
ADD init /bin
CMD ["/bin/init"]
EXPOSE 22
