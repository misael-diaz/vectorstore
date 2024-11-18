FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    vim \
    build-essential \
    git \
    net-tools \
    curl \
    rsync \
    gdb \
    gcc \
    g++
WORKDIR /app
RUN curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o \
    /tmp/miniconda.sh && \
    /bin/bash /tmp/miniconda.sh -b -p /opt/miniconda && \
    rm /tmp/miniconda.sh
ENV PATH="/opt/miniconda/bin:${PATH}"
RUN conda update -n base -c defaults conda
RUN conda install --channel conda-forge --channel omnia \
    chromadb \
    ollama-python \
    ipython
ADD .env /app/.env
ADD doc.txt /app/doc.txt
ADD main.py /app/main.py
CMD /bin/bash
