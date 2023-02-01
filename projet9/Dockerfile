

ARG registry=docker-registry.ign.fr
#ARG PYTHON_VERSION

FROM ${registry}/ign/miniconda3:python-3.9

RUN mamba install --yes \
   proj \
   fiona \
   geopandas \
   psycopg2 \
   geoalchemy2 \
   tqdm \
   -c conda-forge

ENV PROJ_LIB="/opt/conda/share/proj"
