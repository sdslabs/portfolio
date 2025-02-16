FROM python:3.7-buster

ENV PYTHONBUFFERED 1

RUN apt update \
    && apt install libexempi8 \
    && mkdir -p /var/log/portfolio.log

WORKDIR /portfolio

# Install Python dependency management tools
RUN pip install --upgrade pip \
    && pip install --upgrade setuptools 

# Copy the requirements.txt into the container
COPY settings/requirements-common.txt /portfolio/
COPY settings/dev/requirements-dev.txt /portfolio/

# Install the dependencies system-wide
# TODO: Use build args to avoid installing dev dependencies in production
RUN pip install -r requirements-common.txt
RUN pip install -r requirements-dev.txt
