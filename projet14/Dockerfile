


ARG registry=docker-registry.ign.fr
ARG py_version=3.9
ARG condaenv=bdf-mesh-env

FROM ${registry}/ign/miniconda3:python-${py_version}

COPY . .

#RUN conda create --name bdf-mesh-env
RUN mamba env update --file environment.yml && conda clean -tipy

RUN conda init bash
#RUN conda run -n bdf-mesh-env

RUN echo "conda activate bdf-mesh-env" >> ~/.bashrc

#RUN conda activate bdf-mesh-env


##RUN mamba install environment.yml

##  && conda clean -tipy

## RUN mamba env create --file environment.yml && rm -rf ~/.conda/pkgs/*

ENV PROJ_LIB='/opt/conda/share/proj'

