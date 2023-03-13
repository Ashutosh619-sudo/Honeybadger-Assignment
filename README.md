# Honeybadger-Assignment


## Add your slack token and channel name in the .env file.


Steps to the run the it locally:

1) docker-compose build
2) docker-compose up


The enpoint to send the spam notification is http://127.0.0.1:8000/api/alert/.
Using celery for asynchronous distribution of the alert sending task. To monitor all the celery workers using flower.
To see flower dashboard go to http://127.0.0.1:8888/.
