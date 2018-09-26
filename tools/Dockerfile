FROM ubuntu:18.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update
RUN apt-get -y install git
RUN apt-get -y install vim
RUN apt-get -y install nano
COPY .nanorc /root/.nanorc
COPY .gitconfig /root/.gitconfig
