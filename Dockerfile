FROM quay.io/jupyter/base-notebook:latest

USER root

RUN apt-get update --yes && \
    apt-get install --yes --no-install-recommends \
    python3-dev git python-pip postgresql-client gcc

# Set the working directory inside the container
WORKDIR /home/jovyan/alhazen

# Copy the library files to the working directory
COPY . /home/jovyan/alhazen

RUN pip install hatch

USER ${NB_UID}

RUN pip install -e .

CMD start-notebook.py & marimo edit marimo/000_metadata_extraction_map.py --host 0.0.0.0 -p 6720 --token --token-password="everyone"