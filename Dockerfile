FROM python:3.6
COPY apiDamnificado/requirements.txt /apiDamnificado/requirements.txt
RUN pip install -r /apiDamnificado/requirements.txt
WORKDIR /apiDamnificados
COPY apiDamnificado /apiDamnificados
CMD sh migrateDB.sh