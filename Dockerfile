FROM artifactory.apps.bancolombia.com/devops/python:3.7.9-slim-buster
#FROM python:3.7.9-slim-buster

USER root
COPY . .
RUN pip install -r requirements.txt -i https://artifactory.apps.bancolombia.com/api/pypi/pypi-bancolombia/simple --trusted-host artifactory.bancolombia.corp
#RUN pip install -r requirements.txt


#Expose port
EXPOSE 8080

RUN rm -rf /usr/local/lib/python3.7/site-packages/scrapyrt/conf/default_settings.py
COPY ./default_settings.py /usr/local/lib/python3.7/site-packages/scrapyrt/conf

RUN rm -rf /usr/local/lib/python3.7/site-packages/scrapyrt/resources.py
COPY ./resources.py /usr/local/lib/python3.7/site-packages/scrapyrt

RUN mkdir -p /opt/externalSources
COPY externalSources/ /opt/externalSources

WORKDIR /opt/externalSources/projects/sancionesejec/scrapyEjecutariadas

ENTRYPOINT ["scrapyrt","-i","0.0.0.0", "-p", "8080" ]