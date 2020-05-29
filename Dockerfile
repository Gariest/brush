FROM python:3.6

RUN pip install --trusted-host pypi.python.org gunicorn[gevent]

RUN pip install --trusted-host pypi.python.org opencv-contrib-python

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./gunicorn_conf.py /gunicorn_conf.py

#COPY ./gunicorn-master /gunicorn-master

COPY ./app /app

#WORKDIR /gunicorn-master 

#RUN python setup.py install

#WORKDIR ../app/

WORKDIR /app/

ENV PYTHONPATH=/app

EXPOSE 84 85

ENTRYPOINT ["/entrypoint.sh"]

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Meinheld
CMD ["/start.sh"]