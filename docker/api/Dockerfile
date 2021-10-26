FROM ubuntu:20.04


# install apt packages
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y --no-install-recommends \
        build-essential \
        software-properties-common \
        pkg-config \
        curl \
        wget \
        libpq-dev \
        supervisor \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# python install
WORKDIR /tmp
RUN curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -b -p /root/conda
ENV PATH "/root/conda/bin:$PATH"
COPY docker/api/environment.yml /tmp/environment.yml
RUN conda env create -f environment.yml && \
    conda init bash && \
    conda clean -a
RUN echo "conda activate nb-iot-mts" >> ~/.bashrc

# copy environment
RUN mkdir /root/nb-iot-mts
WORKDIR /root/nb-iot-mts
COPY docker/api/supervisor /etc/supervisor/conf.d/
COPY src /root/nb-iot-mts/src/
COPY config.json /root/nb-iot-mts/

# expose api ports
EXPOSE ${API_WEB_PORT}
EXPOSE ${API_COAP_PORT}

CMD ["supervisord", "-n"]