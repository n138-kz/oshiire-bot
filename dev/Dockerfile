FROM python:3

WORKDIR /tmp

RUN set -x && \
	pip install requests

COPY push.py /tmp/
COPY images_001.png /tmp/

CMD ["python3", "push.py"]
