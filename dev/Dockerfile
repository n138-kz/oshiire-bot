FROM python:3

WORKDIR /tmp

RUN set -x && \
	pip install requests

RUN set -x && \
	pip install pyyaml

COPY push.py /tmp/
COPY config.yml /tmp/
COPY images_001.png /tmp/

CMD ["python3", "push.py"]
