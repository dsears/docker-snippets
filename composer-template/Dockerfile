FROM ubuntu:18.04

# prep apt
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update

# install apache
RUN apt-get install apache2 -y && \
    rm /var/www/html/index.html

# install php
RUN apt-get install php libapache2-mod-php -y

# install composer
ENV COMPOSER_ALLOW_SUPERUSER=1
ENV COMPOSER_NO_INTERACTION=1
RUN apt-get -y install curl zip git php-xml php7.2-mbstring && \
    curl --silent --show-error https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer

# clean up apt
RUN apt-get clean
