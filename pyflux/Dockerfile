FROM python:3.6

ADD help.py /
ADD pyflux.py /
RUN pip install influxdb psutil

CMD [ "python", "pyflux.py" ]

