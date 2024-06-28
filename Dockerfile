FROM quay.io/jupyter/base-notebook:latest

USER root

RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    git python-pip postgresql-client

# Set the working directory inside the container
WORKDIR /home/jovyan/alhazen

ENV GRANT_SUDO="yes"

# Copy the library files to the working directory
COPY . /home/jovyan/alhazen

RUN pip install hatch

USER ${NB_UID}

RUN pip install -e .