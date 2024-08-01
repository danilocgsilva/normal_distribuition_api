FROM debian:bookworm-slim

ENV FLASK_APP=/app/app.py
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3-pip -y
RUN pip install -U flask --break-system-packages
RUN pip install numpy --break-system-packages

## Just to run, keep in this state!
CMD flask run

## Otherwise, for development, commend above CMD and uncommend the below one. So, you can enter in the container and debug.
# CMD while : ; do sleep 1000; done