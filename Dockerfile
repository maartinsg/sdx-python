FROM python:2.7
ADD ainars/restapid/rest.py /
RUN pop install flask flask_restful
CMD [ "python", "./rest.py" ]
