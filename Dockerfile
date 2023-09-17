FROM python:3.11.5

RUN mkdir /etc/simwatch
ADD application.toml /etc/simwatch/application.toml
ADD app /opt/app
ADD .shellrc.py /opt/.shellrc.py
ADD crcmd.py /opt/crcmd.py
ADD requirements.txt /opt/requirements.txt

WORKDIR /opt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV CROYDON_CONFIG=/etc/simwatch/application.toml
CMD ["python3.11", "crcmd.py", "run"]
