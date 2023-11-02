FROM alpine:latest
RUN apk add python3
ENV WELCOME_MSG Welcome to my python application in Docker!!
EXPOSE 80
RUN mkdir /app
ADD hello-world.py /app
WORKDIR /app
ENTRYPOINT ["python", "hello-world.py"]