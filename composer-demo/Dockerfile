FROM composer-template

# install composer dependencies
COPY composer.json /var/www/html/composer.json
RUN cd /var/www/html && composer install && rm composer.*

# copy my app
COPY app/ /var/www/html/

# run apache
EXPOSE 80
CMD apachectl -D FOREGROUND
