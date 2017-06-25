# Use an official Python runtime as a base image
FROM python:3.6-slim

MAINTAINER Steven Knight <steven@knight.cx>

RUN apt-get -y update
RUN apt-get -y install libreadline-dev build-essential

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

RUN pip3 install pypoet
RUN poet make:requirements
RUN pip3 install -r requirements.txt

# Run app.py when the container launches
CMD ["python3.6", "eche.py"]
